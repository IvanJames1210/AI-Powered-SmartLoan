import csv

from loan_logic import evaluate_loan_application


REQUIRED_FIELDS = [
    "age",
    "monthly_income",
    "monthly_expenses",
    "existing_loan_amount",
    "existing_monthly_debt_payment",
    "employment_status",
    "employment_duration",
    "credit_score",
    "bank_balance",
    "missed_payments",
    "requested_loan_amount",
    "requested_loan_duration",
]


INTEGER_FIELDS = [
    "age",
    "employment_duration",
    "credit_score",
    "missed_payments",
    "requested_loan_duration",
]


FLOAT_FIELDS = [
    "monthly_income",
    "monthly_expenses",
    "existing_loan_amount",
    "existing_monthly_debt_payment",
    "bank_balance",
    "requested_loan_amount",
]


def read_csv_applications(file_path):
    applications = []

    with open(file_path, mode="r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row_number, row in enumerate(reader, start=2):
            applications.append({
                "row_number": row_number,
                "data": row
            })

    return applications


def validate_missing_values(row):
    errors = []

    for field in REQUIRED_FIELDS:
        if field not in row or row[field] == "":
            errors.append(f"{field} is missing")

    return errors


def convert_csv_row_types(row):
    converted_row = row.copy()

    for field in INTEGER_FIELDS:
        converted_row[field] = int(converted_row[field])

    for field in FLOAT_FIELDS:
        converted_row[field] = float(converted_row[field])

    return converted_row


def validate_unrealistic_values(row):
    errors = []

    if row["age"] < 18 or row["age"] > 100:
        errors.append("age must be between 18 and 100")

    if row["monthly_income"] <= 0:
        errors.append("monthly_income must be greater than 0")

    if row["monthly_expenses"] < 0:
        errors.append("monthly_expenses cannot be negative")

    if row["credit_score"] < 300 or row["credit_score"] > 850:
        errors.append("credit_score must be between 300 and 850")

    if row["requested_loan_amount"] <= 0:
        errors.append("requested_loan_amount must be greater than 0")

    if row["requested_loan_duration"] <= 0:
        errors.append("requested_loan_duration must be greater than 0")

    return errors


def create_duplicate_key(row):
    return tuple(row[field] for field in REQUIRED_FIELDS)


def detect_duplicate_application(row, seen_applications):
    errors = []

    duplicate_key = create_duplicate_key(row)

    if duplicate_key in seen_applications:
        errors.append("duplicate application found")
    else:
        seen_applications.add(duplicate_key)

    return errors


def process_csv_applications(file_path):
    rows = read_csv_applications(file_path)
    results = []
    seen_applications = set()

    for row in rows:
        row_number = row["row_number"]
        raw_data = row["data"]

        missing_errors = validate_missing_values(raw_data)

        if missing_errors:
            results.append({
                "row_number": row_number,
                "status": "validation_error",
                "errors": missing_errors
            })
            continue

        converted_data = convert_csv_row_types(raw_data)

        unrealistic_errors = validate_unrealistic_values(converted_data)
        duplicate_errors = detect_duplicate_application(converted_data, seen_applications)

        all_errors = unrealistic_errors + duplicate_errors

        if all_errors:
            results.append({
                "row_number": row_number,
                "status": "validation_error",
                "errors": all_errors
            })
        else:
            decision_result = evaluate_loan_application(converted_data)

            results.append({
                "row_number": row_number,
                "status": "processed",
                "data": converted_data,
                "decision_result": decision_result
            })

    return results