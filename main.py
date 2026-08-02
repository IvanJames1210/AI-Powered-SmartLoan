# Import FastAPI to create the API application
# Import Request so we can handle validation error requests
from fastapi import FastAPI, Request

# Import FastAPI's validation error class
# This is triggered when the request body does not match the Pydantic model
from fastapi.exceptions import RequestValidationError

# Import JSONResponse so we can return a custom JSON error response
from fastapi.responses import JSONResponse

# Import the main loan evaluation function from loan_logic.py
from loan_logic import evaluate_loan_application

#import database function to save evaluated loan applications
from database import save_loan_application, get_all_loan_applications

# Import Pydantic models from models.py
# These models define request data, successful response data, and validation error data
from models import (
    LoanApplicationRequest,
    LoanDecisionResponse,
    LoanValidationErrorResponse
)

import os
import tempfile

from fastapi import UploadFile, File
from csv_processor import process_csv_applications 


# Create the FastAPI application
app = FastAPI()

# Custom handler for request validation errors
# This runs when the customer sends missing or invalid input
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
# Create an empty list to store readable validation error messages
    errors = []

# Loop through each validation error returned by FastAPI / Pydantic
    for error in exc.errors():
        # Get the field name that caused the error
        field_name = error["loc"][-1]
        # Get the validation message
        message = error["msg"]
        # Add a readable error message to the errors list
        errors.append(f"{field_name}: {message}")

# Create a structured validation error response using the Pydantic model
    response = LoanValidationErrorResponse(
        is_valid=False,
        errors=errors,
        decision_category="validation_error",
        input_source="customer_api_json"
    )
# Return the validation error response with HTTP status code 422
    return JSONResponse(
        status_code=422,
        content=response.model_dump()
    )

# Basic home route to confirm the API is running
@app.get("/")
def home():
    return {"message": "SmartLoan API is running"}


# Main loan evaluation endpoint
# It accepts customer loan application data and returns a loan decision response
@app.post("/loan/evaluate", response_model=LoanDecisionResponse)
def evaluate_loan(applicant: LoanApplicationRequest):
    # Convert the Pydantic request model into a normal Python dictionary
    applicant_data = applicant.model_dump()

    # Send the applicant data to the loan logic function
    result = evaluate_loan_application(applicant_data)

    # Save the applicant data and decision result in the database
    application_id = save_loan_application(applicant_data, result)

    # Add the saved database ID to the API response
    result["application_id"] = application_id

    # Return the final result to the API user
    return result

@app.get("/loan/applications")
def view_loan_applications():
    return get_all_loan_applications()


# Route to upload and process loan applications from a CSV file
@app.post("/loan/evaluate-csv")
async def evaluate_csv_applications(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        return {
            "status": "error",
            "message": "Only CSV files are supported"
        }

    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_file_path = temp_file.name

    try:
        results = process_csv_applications(temp_file_path)
    finally:
        os.remove(temp_file_path)

    return {
        "filename": file.filename,
        "total_rows": len(results),
        "results": results
    }

    