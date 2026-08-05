# SmartLoan Technical Build Documentation

## Document Purpose

This document explains how SmartLoan is being built from a technical point of view.

It records the main files, backend logic, API endpoints, validation, testing, database work, CSV processing, and synthetic data generation added during the build.

---

## Build Stage 1 — Project Foundation

### Technical work completed

The SmartLoan Python project was created with a clear backend structure.

### Main purpose

This stage created the starting point for the project and prepared it for backend development, testing, documentation, and version control.

### Key result

The project had a working local folder structure and Git repository.

---

## Build Stage 2 — Customer Journey and Use Cases

### Technical work completed

The expected loan application flow was planned before building the API.

### Main purpose

This helped define what data the backend needs to receive and what type of response it should return.

### Key result

The system had clear use cases for:

- approved applications
- rejected applications
- invalid applications

---

## Build Stage 3 — First Rule-Based FastAPI Prototype

### Technical work completed

A FastAPI backend was created with a loan evaluation endpoint.

### Main files involved

- `main.py`
- `loan_logic.py`

### Main API endpoint

```text
POST /loan/evaluate
```

### Key result

SmartLoan could receive applicant data as JSON and return a loan approval or rejection decision.

---

## Build Stage 4 — Requirements and Decision Refinement

### Technical work completed

The application fields, validation expectations, risk levels, and decision categories were refined.

### Main purpose

This made the loan decision process more structured and easier to test.

### Key result

SmartLoan had clearer rules for validation, approval, rejection, and risk scoring.

---

## Build Stage 5 — Backend Cleanup and Scoring Review

### Technical work completed

The backend logic was cleaned and the response format was improved.

### Main response fields

- `decision`
- `decision_category`
- `risk_level`
- `risk_score`
- `reasons`
- `input_source`

### Key result

SmartLoan returned clearer and more useful decision responses.

---

## Build Stage 6 — Pydantic Request and Response Models

### Technical work completed

Pydantic models were added to structure API input and output.

### Main file involved

- `models.py`

### Main purpose

The models helped validate applicant data before it reached the loan decision logic.

### Key result

Invalid data could be rejected early with clear validation errors.

---

## Build Stage 7 — Pytest and Automated Testing

### Technical work completed

Automated backend tests were added using Pytest and FastAPI TestClient.

### Main test file

- `tests/test_api.py`

### Test coverage included

- home route
- approved applicant
- rejected applicants
- low credit score
- missed payments
- high debt
- high expenses
- invalid input
- validation errors

### Key result

SmartLoan had automated tests to confirm the backend continued working correctly.

---

## Build Stage 8 — Database Integration

### Technical work completed

SQLite database storage was added for loan applications and decision results.

### Main files involved

- `database.py`
- `migrations/001_create_loan_applications.sql`

### Main database table

```text
loan_applications
```

### Main API endpoint added

```text
GET /loan/applications
```

### Stored information

- applicant input data
- decision result
- risk score
- risk level
- decision reasons
- input source
- timestamp

### Key result

SmartLoan could save and view previous loan application decisions.

---

## Build Stage 9 — CSV Processing and Data Quality

### Technical work completed

CSV batch processing was added so multiple loan applications could be processed together.

### Main files involved

- `csv_processor.py`
- `data/sample_applications.csv`
- `tests/test_csv_processing.py`

### Main API endpoint added

```text
POST /loan/evaluate-csv
```

### Data-quality checks included

- missing values
- unrealistic values
- duplicate applications
- row-by-row validation
- row-by-row batch results

### Key result

SmartLoan could process loan applications in bulk through CSV files.

---

## Build Stage 10 — Synthetic and Mock Data

### Technical work completed

Synthetic loan applicant data generation was added.

### Main files involved

- `synthetic_data_generator.py`
- `data/synthetic_applications.csv`
- `tests/test_synthetic_data_generator.py`

### Synthetic applicant types

- low-risk applicants
- medium-risk applicants
- high-risk applicants

### Main purpose

Synthetic data allows SmartLoan to be tested without using real customer information.

### Key result

SmartLoan could generate 100 fake loan applicant records for testing and model preparation.

---

## Current API Endpoints

```text
GET /
POST /loan/evaluate
GET /loan/applications
POST /loan/evaluate-csv
```

---

## Current Main Project Files

```text
main.py
models.py
loan_logic.py
database.py
csv_processor.py
synthetic_data_generator.py
```

---

## Current Testing Files

```text
tests/test_api.py
tests/test_csv_processing.py
tests/test_synthetic_data_generator.py
```

---

## Current Data Files

```text
data/sample_applications.csv
data/synthetic_applications.csv
```

---

## Current Database and Migration Files

```text
database.py
migrations/001_create_loan_applications.sql
```

---

## Latest Test Result

```text
24 passed
```

---

## Technical Summary

SmartLoan currently has a working FastAPI backend with structured request and response models, rule-based decision logic, automated testing, database storage, CSV batch processing, and synthetic data generation.

The project is being built step by step as a complete loan eligibility and risk assessment system.