# AI-Powered SmartLoan

## Project Overview

AI-Powered SmartLoan Version 1.0 is a backend prototype developed through Iterations 1–8 for evaluating basic loan eligibility and risk.

The prototype accepts customer loan application data, validates the input, applies simple rule-based risk checks, saves valid loan applications in a local database, and returns a structured JSON response with:

• Application ID  
• Decision: Approved or Rejected  
• Risk level: Low, Medium or High  
• Risk score  
• Reasons for the decision  
• Validation errors when input is missing or invalid  

This version is focused on backend logic, API testing, automated testing, and local database storage.

## Current Scope

This prototype includes:

• Python loan evaluation logic  
• Input validation  
• Rule-based risk scoring  
• FastAPI backend  
• POST API endpoint for loan evaluation  
• GET API endpoint for saved loan applications  
• Swagger testing  
• Postman test collection  
• Testing notes  
• Pydantic request and response models  
• Automatic data-type and value validation  
• Structured validation-error responses  
• SQLite database storage  
• Saved loan applications route  
• Database application ID returned in API response  
• Automated testing with Pytest  

## Automated Decision Policy

SmartLoan currently makes loan decisions automatically without a human loan officer or manual review.

The current decision policy is:

• Approved: The application is valid and no risk factors are identified.  
• Rejected: The application is valid but one or more risk factors are identified.  
• Validation Error: Required data is missing or invalid, so the system does not make an approval or rejection decision.  

The current system does not use:

• Manual review  
• Loan officer approval  
• Review Required  
• More Information Required  

All current decisions are made automatically using validation rules and rule-based risk checks.

## Current Limitations

The current SmartLoan Version 1.0 prototype, developed through Iterations 1–8, does not include:

• Frontend user interface  
• Real bank integrations  
• Real credit bureau checks  
• Employer or KYC verification  
• PDF, image, or CSV/Excel processing  
• Manual review workflow  
• Full AI/ML model  
• Production-level authentication and security  

## Use Cases

The current tests are mapped to the SmartLoan Version 1.0 use cases:

UC1 — Good Applicant - Approved  
UC2 — Missed Payments - Rejected  
UC3 — Low Credit Score - Rejected  
UC4 — High Debt - Rejected  
UC5 — High Expenses - Rejected  
UC6 — Loan Amount Too High - Rejected  
UC7 — Multiple Risk Factors - High Risk  
UC8 — Missing or Invalid Application Data  
UC9 — Saved Loan Applications - Database Records  

## Current Input Source

SmartLoan Version 1.0 uses customer-provided API/JSON data only.

The system validates the submitted values and applies rule-based eligibility and risk checks. It does not currently verify information through external documents or third-party systems.

## Future Input Sources

Future iterations may explore:

• Synthetic or sandbox bank transaction data  
• Mock credit bureau data  
• Mock employer and KYC verification data  
• PDF documents such as bank statements and payslips  
• Images such as ID cards and document screenshots  
• CSV/Excel applicant and financial records  

These sources are future scope and are not processed by SmartLoan Version 1.0.

## Project Files

| File                | Purpose                                                        |
| ------------------- | -------------------------------------------------------------- |
| `loan_logic.py`     | Contains validation, risk scoring, and decision logic          |
| `main.py`           | Contains the FastAPI app and API routes                        |
| `models.py`         | Contains Pydantic request, response, and validation models     |
| `database.py`       | Contains SQLite database creation, save, and read logic        |
| `tests/test_api.py` | Contains automated Pytest API tests                            |
| `TESTING_NOTES.md`  | Contains the testing summary and test cases                    |
| `SCORING_RULES.md`  | Contains the scoring rules used by the decision logic          |
| `.gitignore`        | Prevents local files like `smartloan.db` from being pushed     |

## API Endpoints

### Health Check

```http
GET /
```

Returns a basic message confirming that the API is running.

### Loan Evaluation

```http
POST /loan/evaluate
```

Local URL:

```text
http://127.0.0.1:8002/loan/evaluate
```

This endpoint accepts applicant data as JSON, validates the input, evaluates loan risk, saves the application and decision in the database, and returns the loan evaluation result.

### Saved Loan Applications

```http
GET /loan/applications
```

Local URL:

```text
http://127.0.0.1:8002/loan/applications
```

This endpoint returns all saved loan applications from the local SQLite database.

## Sample Request

```json
{
  "age": 28,
  "monthly_income": 12000,
  "monthly_expenses": 4000,
  "existing_loan_amount": 5000,
  "existing_monthly_debt_payment": 1000,
  "employment_status": "employed",
  "employment_duration": 24,
  "credit_score": 720,
  "bank_balance": 8000,
  "missed_payments": 0,
  "requested_loan_amount": 20000,
  "requested_loan_duration": 12
}
```

## Sample Response

```json
{
  "application_id": 1,
  "decision": "Approved",
  "decision_category": "approval",
  "risk_level": "Low",
  "risk_score": 0,
  "reasons": [
    "Existing debt level is acceptable.",
    "Monthly expenses are acceptable.",
    "Credit score is acceptable.",
    "No missed payments found.",
    "Requested loan amount is acceptable."
  ],
  "input_source": "customer_api_json"
}
```

## How to Run the Project

From the project folder, run:

```bash
uvicorn main:app --reload --port 8002
```

Then open Swagger:

```text
http://127.0.0.1:8002/docs
```

Or test the API in Postman using:

```text
POST http://127.0.0.1:8002/loan/evaluate
```

and:

```text
GET http://127.0.0.1:8002/loan/applications
```

## Testing Summary

The API was tested using Swagger, Postman, and Pytest.

Pydantic validation was tested for missing fields, incorrect data types, invalid value ranges, and structured HTTP 422 validation responses.

Postman test cases include:

• Home route → API running  
• Good applicant → Approved with application ID  
• Rejected applicant → Rejected with application ID  
• Saved applications → Database records returned  
• Invalid applicant → Validation error  

All planned Swagger, Postman, and Pytest tests returned the expected status codes and JSON responses.

## Automated Testing with Pytest

Automated API tests were added using Pytest and FastAPI TestClient.

The tests are stored in:

```text
tests/test_api.py
```

Current automated tests cover:

- Home route check
- Good applicant approval
- Application ID returned after saving to database
- Missed payments rejection
- Low credit score rejection
- High debt rejection
- High expenses rejection
- Loan amount too high rejection
- Multiple risk factors high-risk rejection
- Missing input validation error
- Invalid credit score validation error
- Underage applicant validation error
- Zero income validation error
- Negative expenses validation error
- Saved loan applications database route

To run all automated tests:

```bash
python -m pytest
```

Latest Pytest result:

```text
14 passed
```

## Iteration 8: Database Integration

In Iteration 8, SmartLoan was updated to save loan applications and decisions in a local SQLite database.

### Database Used

SmartLoan now uses SQLite for local database storage.

Database file:

```text
smartloan.db
```

This file is generated locally and is not pushed to GitHub.

### What is Saved

Each loan application saves:

- applicant input data
- final decision
- decision category
- risk level
- risk score
- decision reasons
- input source
- created timestamp

### Updated Loan Evaluation Endpoint

```http
POST /loan/evaluate
```

This endpoint now:

1. validates applicant input
2. evaluates loan risk
3. saves the application and decision in the database
4. returns a unique `application_id`

### New Saved Applications Endpoint

```http
GET /loan/applications
```

This endpoint returns all saved loan applications from the database.

It is used to confirm that SmartLoan can store and retrieve loan application records.

### Local Database Note

The database file is ignored by Git using `.gitignore`:

```text
smartloan.db
```

This keeps local test data out of GitHub.

## Current Status

SmartLoan Version 1.0 is working locally through FastAPI.

Completed so far:

- loan eligibility and risk scoring logic
- request and response validation with Pydantic
- Swagger testing
- Postman testing
- Pytest automated testing
- SQLite database storage
- saved loan applications route

## Next Possible Improvements

- Add more detailed repayment-ability logic
- Add future evidence-verification logic in a later iteration
- Improve database testing with a separate test database
- Continue improving API documentation

## Database Design and Future PostgreSQL Plan

SmartLoan currently uses SQLite for local development.

Current database file:

```text
smartloan.db
```

Current table:

```text
loan_applications
```

For the current prototype, one combined table is used. This table stores both applicant data and decision data together.

A basic migration file has also been added:

```text
migrations/001_create_loan_applications.sql
```

This file documents how the loan_applications table is created.

### Future PostgreSQL Support

In a future production version, SmartLoan can move from SQLite to PostgreSQL.

Future PostgreSQL improvements may include:

- using PostgreSQL instead of SQLite
- storing database connection settings in environment variables
- using database migration tools such as Alembic
- creating separate tables for loan applications and loan decisions

### Future Separate Table Design

The current prototype uses one table:

```text
loan_applications
```

A future version can separate this into two tables:

```text
loan_applications
loan_decisions
```

Simple future design:

- loan_applications stores applicant input details
- loan_decisions stores decision result, risk score, reasons, and timestamp

## Iteration 9: CSV Processing and Data Quality

In Iteration 9, SmartLoan was updated to process multiple loan applications from a CSV file.

Before this iteration, SmartLoan mainly evaluated one applicant at a time using JSON.

Now SmartLoan can read a CSV file, validate each row, process valid applications, and return row-by-row batch results.

### CSV Sample File

A sample CSV file was added:

```text
data/sample_applications.csv


The sample file includes:

- valid applicant records
- a missing-value record
- an unrealistic-value record
- a duplicate application record

### CSV Processing Logic

A new file was added:

```text
csv_processor.py
```

This file handles:

- reading customer applications from CSV
- validating required fields
- detecting missing values
- converting CSV text values into Python numbers
- detecting unrealistic values
- detecting duplicate applications
- processing valid rows through the SmartLoan decision logic
- returning batch-processing results

### New CSV Evaluation Endpoint

```http
POST /loan/evaluate-csv
```

This endpoint accepts a CSV file upload and returns results for each row.

Example result types:

- processed
- validation_error

### CSV Testing

Iteration 9 was tested using:

- Terminal
- Swagger
- Postman
- Pytest

Latest Pytest result:

```text
20 passed
```

### Iteration 9 Result

SmartLoan can now process bulk loan applications from a CSV file, validate each row, detect data-quality issues, detect duplicate applications, and return clear batch-processing results.