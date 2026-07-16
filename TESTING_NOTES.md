# AI-Powered SmartLoan — Testing Notes

## Endpoint Tested

Main loan evaluation endpoint:

```http
POST /loan/evaluate
```

Local test URL:

```text
http://127.0.0.1:8002/loan/evaluate
```

Saved applications endpoint:

```http
GET /loan/applications
```

Local test URL:

```text
http://127.0.0.1:8002/loan/applications
```

## Testing Tools

SmartLoan was tested using:

- Swagger
- Postman
- Pytest with FastAPI TestClient

## Test Summary

The API was tested using Swagger, Postman, and automated Pytest tests.

The endpoint uses Pydantic to validate applicant data before applying rule-based risk checks and returning a structured JSON response.

In Iteration 8, SQLite database integration was added and tested.

The testing confirmed that:

- valid loan applications are evaluated correctly
- valid loan applications are saved in the database
- the API returns an `application_id`
- saved applications can be viewed through `GET /loan/applications`
- invalid applications return validation errors
- invalid applications are blocked before normal loan decision/database saving

## Test Cases Covered

| Test Case                               | Input Change                                 | Expected Result                              |
| --------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| Home Route - API Running                | GET `/`                                      | API running message                          |
| Good Applicant - Approved               | Normal applicant data                        | Approved, Low risk, risk score 0, application ID |
| Missed Payments - Rejected              | `missed_payments = 1`                        | Rejected, Medium risk                        |
| Low Credit Score - Rejected             | `credit_score = 520`                         | Rejected, Medium risk                        |
| High Debt - Rejected                    | `existing_monthly_debt_payment = 6000`       | Rejected, Medium risk                        |
| High Expenses - Rejected                | `monthly_expenses = 8000`                    | Rejected, Medium risk                        |
| Loan Amount Too High - Rejected         | `requested_loan_amount = 50000`              | Rejected, Medium risk                        |
| Multiple Risk Factors - High Risk       | Low credit score, missed payments, high debt | Rejected, High risk                          |
| Missing Input - Validation Error        | Removed `bank_balance`                       | Validation error                             |
| Invalid Credit Score - Validation Error | `credit_score = 900`                         | Validation error                             |
| Underage Applicant - Validation Error   | `age = 16`                                   | Validation error                             |
| Zero Income - Validation Error          | `monthly_income = 0`                         | Validation error                             |
| Negative Expenses - Validation Error    | `monthly_expenses = -1000`                   | Validation error                             |
| Saved Loan Applications                 | GET `/loan/applications`                     | Saved database records returned             |

## Use Case Mapping

The test cases are mapped to the SmartLoan Version 1.0 use cases as follows:

- UC1 — Good Applicant - Approved
- UC2 — Missed Payments - Rejected
- UC3 — Low Credit Score - Rejected
- UC4 — High Debt - Rejected
- UC5 — High Expenses - Rejected
- UC6 — Loan Amount Too High - Rejected
- UC7 — Multiple Risk Factors - High Risk
- UC8 — Missing or Invalid Application Data
- UC9 — Saved Loan Applications - Database Records

UC8 includes:

- Missing Input - Validation Error
- Invalid Credit Score - Validation Error
- Underage Applicant - Validation Error
- Zero Income - Validation Error
- Negative Expenses - Validation Error

The current tests use customer-provided API/JSON data only. SmartLoan Version 1.0 does not verify external documents or third-party data.

## API Response Fields

The SmartLoan API response includes:

- `application_id` - unique database ID for saved valid applications
- `decision` - Approved or Rejected
- `decision_category` - approval, rejection, or validation_error
- `risk_level` - Low, Medium, or High
- `risk_score` - numeric risk score
- `reasons` - explanation for the decision
- `input_source` - source of submitted data

Current values:

- Approved application → `decision_category: approval`
- Rejected application → `decision_category: rejection`
- Invalid application → `decision_category: validation_error`
- Current input source → `input_source: customer_api_json`

Invalid applications do not return an `application_id` because they are blocked before normal loan evaluation and database saving.

## Swagger Testing

Swagger was used to manually test the updated API endpoints.

### POST /loan/evaluate

A valid good applicant was submitted.

Expected result:

- Status code: 200
- Decision: Approved
- Decision category: approval
- Risk level: Low
- Risk score: 0
- Response includes `application_id`

Result: Passed

### GET /loan/applications

The saved applications endpoint was tested.

Expected result:

- Status code: 200
- Response returns a list of saved loan application records
- Saved records include applicant data, decision result, risk score, reasons, input source, and created timestamp

Result: Passed

## Postman Testing

Postman was used to test the main Iteration 8 API behavior.

Test cases completed:

- Home route → API running
- Good applicant → Approved with database application ID
- Rejected applicant → Rejected with database application ID
- Saved applications route → Database records returned
- Invalid applicant → Validation error

## Validation Error Testing

An invalid applicant was tested using negative monthly expenses.

Expected result:

- Status code: 422
- `is_valid` is false
- `decision_category` is `validation_error`
- error message explains the invalid field
- no `application_id` is returned

Result: Passed

This confirms invalid input is blocked before normal loan decision/database saving.

## Iteration 7 — Automated Pytest Testing

Automated API tests were added using Pytest and FastAPI TestClient.

Test file created:

```text
tests/test_api.py
```

The automated tests cover:

- Home route check
- Good applicant approval
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

## Iteration 8 — Database Integration Testing

Pytest was updated for Iteration 8.

New automated checks include:

- response includes `application_id`
- `application_id` is an integer
- `application_id` is greater than 0
- saved loan applications route returns a list

Command used:

```bash
python -m pytest
```

Latest result:

```text
14 passed
```

## Final Testing Result

All Iteration 8 tests passed successfully.

Database integration is working correctly with:

- FastAPI
- SQLite
- Swagger
- Postman
- Pytest

SmartLoan Version 1.0 is working locally through FastAPI with automated testing and local database storage.