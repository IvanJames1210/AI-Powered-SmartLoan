from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test 1: Check that the SmartLoan API home route is running correctly
def test_home_route():
    response = client.get("/")

    assert response.status_code == 200 
    assert response.json() == {"message": "SmartLoan API is running"}

# Test 2: Check that a good applicant with no risk factors is approved
def test_good_applicant_is_approved():
    applicant = {
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

    response = client.post("/loan/evaluate", json=applicant)

    assert response.status_code == 200
    assert response.json()["decision"] == "Approved"
    assert response.json()["decision_category"] == "approval"
    assert response.json()["risk_level"] == "Low"
    assert response.json()["risk_score"] == 0
    assert response.json()["input_source"] == "customer_api_json"


# Test 3: Check that an applicant with missed payments is rejected
def test_missed_payments_is_rejected():
    applicant = {
        "age": 28,
        "monthly_income": 12000,
        "monthly_expenses": 4000,
        "existing_loan_amount": 5000,
        "existing_monthly_debt_payment": 1000,
        "employment_status": "employed",
        "employment_duration": 24,
        "credit_score": 720,
        "bank_balance": 8000,
        "missed_payments": 1,
        "requested_loan_amount": 20000,
        "requested_loan_duration": 12
    }

    response = client.post("/loan/evaluate", json=applicant)

    assert response.status_code == 200
    assert response.json()["decision"] == "Rejected"
    assert response.json()["decision_category"] == "rejection"
    assert response.json()["risk_level"] == "Medium"
    assert response.json()["risk_score"] == 2
    assert "Missed payments are present." in response.json()["reasons"]


# Test 4: Check that an applicant with a low credit score is rejected
def test_low_credit_score_is_rejected():
    applicant = {
        "age": 28,
        "monthly_income": 12000,
        "monthly_expenses": 4000,
        "existing_loan_amount": 5000,
        "existing_monthly_debt_payment": 1000,
        "employment_status": "employed",
        "employment_duration": 24,
        "credit_score": 520,
        "bank_balance": 8000,
        "missed_payments": 0,
        "requested_loan_amount": 20000,
        "requested_loan_duration": 12
    }

    response = client.post("/loan/evaluate", json=applicant)

    assert response.status_code == 200
    assert response.json()["decision"] == "Rejected"
    assert response.json()["decision_category"] == "rejection"
    assert response.json()["risk_level"] == "Medium"
    assert response.json()["risk_score"] == 2
    assert "Credit score is low." in response.json()["reasons"]


# Test 5: Check that an applicant with high existing monthly debt is rejected
def test_high_debt_is_rejected():
    applicant = {
        "age": 28,
        "monthly_income": 12000,
        "monthly_expenses": 4000,
        "existing_loan_amount": 5000,
        "existing_monthly_debt_payment": 6000,
        "employment_status": "employed",
        "employment_duration": 24,
        "credit_score": 720,
        "bank_balance": 8000,
        "missed_payments": 0,
        "requested_loan_amount": 20000,
        "requested_loan_duration": 12
    }

    response = client.post("/loan/evaluate", json=applicant)

    assert response.status_code == 200
    assert response.json()["decision"] == "Rejected"
    assert response.json()["decision_category"] == "rejection"
    assert response.json()["risk_level"] == "Medium"
    assert response.json()["risk_score"] == 2
    assert "Existing debt is high compared to income." in response.json()["reasons"]


# Test 6: Check that an applicant with high monthly expenses is rejected
def test_high_expenses_is_rejected():
    applicant = {
        "age": 28,
        "monthly_income": 12000,
        "monthly_expenses": 8000,
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

    response = client.post("/loan/evaluate", json=applicant)

    assert response.status_code == 200
    assert response.json()["decision"] == "Rejected"
    assert response.json()["decision_category"] == "rejection"
    assert response.json()["risk_level"] == "Medium"
    assert response.json()["risk_score"] == 2
    assert "Monthly expenses are high compared to income." in response.json()["reasons"]


# Test 7: Check that an applicant requesting too much loan amount is rejected
def test_loan_amount_too_high_is_rejected():
    applicant = {
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
        "requested_loan_amount": 50000,
        "requested_loan_duration": 12
    }

    response = client.post("/loan/evaluate", json=applicant)

    assert response.status_code == 200
    assert response.json()["decision"] == "Rejected"
    assert response.json()["decision_category"] == "rejection"
    assert response.json()["risk_level"] == "Medium"
    assert response.json()["risk_score"] == 2
    assert "Requested loan amount is high compared to income." in response.json()["reasons"]

# Test 8: Check that an applicant with multiple risk factors is rejected as High risk
def test_multiple_risk_factors_is_high_risk():
    applicant = {
        "age": 28,
        "monthly_income": 12000,
        "monthly_expenses": 8000,
        "existing_loan_amount": 5000,
        "existing_monthly_debt_payment": 6000,
        "employment_status": "employed",
        "employment_duration": 24,
        "credit_score": 520,
        "bank_balance": 8000,
        "missed_payments": 1,
        "requested_loan_amount": 50000,
        "requested_loan_duration": 12
    }

    response = client.post("/loan/evaluate", json=applicant)

    assert response.status_code == 200
    assert response.json()["decision"] == "Rejected"
    assert response.json()["decision_category"] == "rejection"
    assert response.json()["risk_level"] == "High"
    assert response.json()["risk_score"] == 10


# Test 9: Check that missing required input returns validation error
def test_missing_input_returns_validation_error():
    applicant = {
        "age": 28,
        "monthly_income": 12000,
        "monthly_expenses": 4000,
        "existing_loan_amount": 5000,
        "existing_monthly_debt_payment": 1000,
        "employment_status": "employed",
        "employment_duration": 24,
        "credit_score": 720,
        "missed_payments": 0,
        "requested_loan_amount": 20000,
        "requested_loan_duration": 12
    }

    response = client.post("/loan/evaluate", json=applicant)

    assert response.status_code == 422
    assert response.json()["is_valid"] is False
    assert response.json()["decision_category"] == "validation_error"
    assert response.json()["input_source"] == "customer_api_json"


# Test 10: Check that invalid credit score returns validation error
def test_invalid_credit_score_returns_validation_error():
    applicant = {
        "age": 28,
        "monthly_income": 12000,
        "monthly_expenses": 4000,
        "existing_loan_amount": 5000,
        "existing_monthly_debt_payment": 1000,
        "employment_status": "employed",
        "employment_duration": 24,
        "credit_score": 900,
        "bank_balance": 8000,
        "missed_payments": 0,
        "requested_loan_amount": 20000,
        "requested_loan_duration": 12
    }

    response = client.post("/loan/evaluate", json=applicant)

    assert response.status_code == 422
    assert response.json()["is_valid"] is False
    assert response.json()["decision_category"] == "validation_error"
    assert response.json()["input_source"] == "customer_api_json"


# Test 11: Check that underage applicant returns validation error
def test_underage_applicant_returns_validation_error():
    applicant = {
        "age": 16,
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

    response = client.post("/loan/evaluate", json=applicant)

    assert response.status_code == 422
    assert response.json()["is_valid"] is False
    assert response.json()["decision_category"] == "validation_error"
    assert response.json()["input_source"] == "customer_api_json"


# Test 12: Check that zero income returns validation error
def test_zero_income_returns_validation_error():
    applicant = {
        "age": 28,
        "monthly_income": 0,
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

    response = client.post("/loan/evaluate", json=applicant)

    assert response.status_code == 422
    assert response.json()["is_valid"] is False
    assert response.json()["decision_category"] == "validation_error"
    assert response.json()["input_source"] == "customer_api_json"


# Test 13: Check that negative expenses return validation error
def test_negative_expenses_returns_validation_error():
    applicant = {
        "age": 28,
        "monthly_income": 12000,
        "monthly_expenses": -1000,
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

    response = client.post("/loan/evaluate", json=applicant)

    assert response.status_code == 422
    assert response.json()["is_valid"] is False
    assert response.json()["decision_category"] == "validation_error"
    assert response.json()["input_source"] == "customer_api_json"