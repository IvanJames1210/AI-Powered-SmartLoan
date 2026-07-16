import sqlite3
import json
from datetime import datetime


DATABASE_NAME = "smartloan.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS loan_applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER NOT NULL,
            monthly_income REAL NOT NULL,
            monthly_expenses REAL NOT NULL,
            existing_loan_amount REAL NOT NULL,
            existing_monthly_debt_payment REAL NOT NULL,
            employment_status TEXT NOT NULL,
            employment_duration INTEGER NOT NULL,
            credit_score INTEGER NOT NULL,
            bank_balance REAL NOT NULL,
            missed_payments INTEGER NOT NULL,
            requested_loan_amount REAL NOT NULL,
            requested_loan_duration INTEGER NOT NULL,
            decision TEXT NOT NULL,
            decision_category TEXT NOT NULL,
            risk_level TEXT NOT NULL,
            risk_score INTEGER NOT NULL,
            reasons TEXT NOT NULL,
            input_source TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_loan_application(applicant_data, decision_result):
    create_database()

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO loan_applications (
            age,
            monthly_income,
            monthly_expenses,
            existing_loan_amount,
            existing_monthly_debt_payment,
            employment_status,
            employment_duration,
            credit_score,
            bank_balance,
            missed_payments,
            requested_loan_amount,
            requested_loan_duration,
            decision,
            decision_category,
            risk_level,
            risk_score,
            reasons,
            input_source,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        applicant_data["age"],
        applicant_data["monthly_income"],
        applicant_data["monthly_expenses"],
        applicant_data["existing_loan_amount"],
        applicant_data["existing_monthly_debt_payment"],
        applicant_data["employment_status"],
        applicant_data["employment_duration"],
        applicant_data["credit_score"],
        applicant_data["bank_balance"],
        applicant_data["missed_payments"],
        applicant_data["requested_loan_amount"],
        applicant_data["requested_loan_duration"],
        decision_result["decision"],
        decision_result["decision_category"],
        decision_result["risk_level"],
        decision_result["risk_score"],
        json.dumps(decision_result["reasons"]),
        decision_result["input_source"],
        datetime.now().isoformat(timespec="seconds")
    ))

    application_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return application_id


def get_all_loan_applications():
    create_database()

    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM loan_applications ORDER BY id DESC")
    rows = cursor.fetchall()

    connection.close()

    applications = []

    for row in rows:
        application = dict(row)
        application["reasons"] = json.loads(application["reasons"])
        applications.append(application)

    return applications