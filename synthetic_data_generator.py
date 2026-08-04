import csv
import random


FIELDNAMES = [
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


def generate_synthetic_applicant():
    applicant_type = random.choice(["low_risk", "medium_risk", "high_risk"])

    if applicant_type == "low_risk":
        monthly_income = random.randint(10000, 20000)
        monthly_expenses = random.randint(2000, 6000)
        credit_score = random.randint(700, 850)
        missed_payments = 0
        existing_monthly_debt_payment = random.randint(0, 2000)
        requested_loan_amount = random.randint(5000, 30000)

    elif applicant_type == "medium_risk":
        monthly_income = random.randint(6000, 12000)
        monthly_expenses = random.randint(3000, 7000)
        credit_score = random.randint(600, 699)
        missed_payments = random.choice([0, 1])
        existing_monthly_debt_payment = random.randint(1000, 4000)
        requested_loan_amount = random.randint(15000, 40000)

    else:
        monthly_income = random.randint(3000, 8000)
        monthly_expenses = random.randint(3000, 7000)
        credit_score = random.randint(300, 599)
        missed_payments = random.randint(1, 4)
        existing_monthly_debt_payment = random.randint(2000, 6000)
        requested_loan_amount = random.randint(25000, 60000)

    return {
        "age": random.randint(18, 70),
        "monthly_income": monthly_income,
        "monthly_expenses": monthly_expenses,
        "existing_loan_amount": random.randint(0, 50000),
        "existing_monthly_debt_payment": existing_monthly_debt_payment,
        "employment_status": random.choice(["employed", "self_employed"]),
        "employment_duration": random.randint(1, 120),
        "credit_score": credit_score,
        "bank_balance": random.randint(500, 50000),
        "missed_payments": missed_payments,
        "requested_loan_amount": requested_loan_amount,
        "requested_loan_duration": random.choice([6, 12, 18, 24, 36]),
    }


def create_synthetic_applications(total_applications):
    applications = []

    for _ in range(total_applications):
        applicant = generate_synthetic_applicant()
        applications.append(applicant)

    return applications


def save_synthetic_applications_to_csv(file_path, total_applications=100):
    applications = create_synthetic_applications(total_applications)

    with open(file_path, mode="w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(applications)

    return len(applications)


if __name__ == "__main__":
    output_file = "data/synthetic_applications.csv"
    total_created = save_synthetic_applications_to_csv(output_file, 100)

    print(f"{total_created} synthetic loan applications created.")
    print(f"File saved to: {output_file}")