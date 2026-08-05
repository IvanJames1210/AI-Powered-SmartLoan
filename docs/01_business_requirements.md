# SmartLoan Business Requirements Document

## 1. Project Overview

SmartLoan is an AI-powered loan eligibility and risk assessment system designed to help evaluate personal loan applications in a structured, consistent, and scalable way.

The project is being built step by step through a full product roadmap, starting from a rule-based backend and gradually expanding into data processing, machine learning, explainability, fairness, monitoring, deployment, and final product readiness.

## 2. Business Problem

Manual loan review can be slow, inconsistent, and difficult to scale.

Different applicants may be assessed differently depending on the reviewer, available information, or manual judgement. This can create delays, increase risk, and make the loan approval process less transparent.

SmartLoan aims to reduce this problem by providing a clear system that checks applicant information, evaluates risk factors, and returns a structured loan decision with reasons.

## 3. Project Goal

The goal of SmartLoan is to support automated loan eligibility and risk evaluation.

The system should be able to:

- receive applicant information
- validate the submitted data
- assess financial and credit-related risk
- return an approval or rejection decision
- explain the main reasons behind the decision
- support both single and batch application processing
- store application and decision history
- generate safe test data for development and model preparation

## 4. Users and Stakeholders

### Loan Applicants

Applicants provide their personal, employment, and financial information to check loan eligibility.

### Lenders or Fintech Business

The lending business uses SmartLoan to support faster and more consistent loan assessment.

### Management and Business Teams

Business teams use the system to improve decision consistency, reduce manual effort, and support better risk control.

### Technical Team

The technical team builds, tests, maintains, and improves the SmartLoan system.

## 5. Applicant Information Required

SmartLoan uses applicant information such as:

- age
- monthly income
- monthly expenses
- existing loan amount
- existing monthly debt payment
- employment status
- employment duration
- credit score
- bank balance
- missed payments
- requested loan amount
- requested loan duration

These fields help the system understand the applicant’s financial position and repayment risk.

## 6. System Outputs

After evaluating an application, SmartLoan returns:

- loan decision: Approved or Rejected
- decision category
- risk score
- risk level
- decision reasons
- input source
- application record ID when saved

The output is designed to be clear enough for business users and structured enough for technical use.

## 7. Main Business Flow

The SmartLoan process follows this flow:

1. The applicant submits loan application information.
2. The system checks whether the information is complete and valid.
3. If the information is invalid, the system returns a validation error.
4. If the information is valid, the system evaluates risk factors.
5. The system returns a loan decision with risk details and reasons.
6. The application and decision can be stored for history and review.
7. Batch applications can be processed through CSV files.
8. Synthetic applicant data can be generated for safe testing and model preparation.

## 8. Loan Decision Requirements

SmartLoan should approve an applicant when the submitted information is valid and does not show major risk indicators.

SmartLoan should reject an applicant when the application shows risk factors such as:

- low credit score
- missed payments
- high existing debt
- high monthly expenses
- requested loan amount too high compared to income
- multiple combined risk factors

The decision should always include clear reasons so the result is understandable.

## 9. Validation Requirements

SmartLoan must validate applicant information before making a loan decision.

The system should stop processing and return a validation error when:

- required information is missing
- applicant age is below the allowed limit
- monthly income is zero or negative
- expenses are negative
- credit score is outside the accepted range
- requested loan amount is zero or negative
- requested loan duration is zero or negative
- financial values are unrealistic or inconsistent

Validation helps prevent incorrect or incomplete data from reaching the decision engine.

## 10. Data Processing Requirements

SmartLoan should support both individual and bulk application processing.

### Single Application Processing

A single applicant can be evaluated through the API using structured applicant data.

### CSV Batch Processing

Multiple applicants can be processed using a CSV file. The system should check every row and identify:

- valid applications
- missing values
- unrealistic values
- duplicate applications
- row-by-row processing results

### Synthetic Data Generation

SmartLoan can generate fake applicant records for safe testing. This allows the project to be tested without using real customer data.

Synthetic data should include different applicant profiles such as:

- low-risk applicants
- medium-risk applicants
- high-risk applicants

## 11. Data Storage Requirements

SmartLoan should store valid loan applications and their decision results.

Stored information should include:

- applicant input data
- decision result
- risk score
- risk level
- decision reasons
- input source
- timestamp

This supports application history, review, auditability, and later analysis.

## 12. Testing and Quality Requirements

SmartLoan should be tested using both manual and automated testing.

Testing should cover:

- approved applications
- rejected applications
- validation errors
- API behaviour
- database storage
- CSV batch processing
- synthetic data generation

Automated testing helps confirm that the system continues to work correctly as the project grows.

## 13. Business Value

SmartLoan provides business value by:

- reducing manual review effort
- improving decision consistency
- making loan decisions easier to explain
- supporting faster applicant evaluation
- improving data quality checks
- creating a foundation for machine-learning-based risk assessment
- supporting scalable financial decisioning

## 14. Product Build Direction

SmartLoan is being developed as one complete product through a structured build roadmap.

The project starts with a clear business problem and a working backend, then continues building stronger data processing, better financial indicators, machine learning, explainability, fairness checks, security, monitoring, deployment, and final product readiness.

Each stage adds another layer to the product, like a ladder, until SmartLoan becomes a complete enterprise-style loan eligibility and risk engine.

## 15. Success Criteria

SmartLoan will be successful if it can:

- accept valid applicant data
- reject invalid or incomplete data clearly
- evaluate loan risk consistently
- return understandable decision reasons
- process both single and batch applications
- store application and decision history
- support safe testing using synthetic data
- grow into a complete AI-powered loan risk assessment system