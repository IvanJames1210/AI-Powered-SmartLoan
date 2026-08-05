# SmartLoan Non-Technical Build Documentation

## Document Purpose

This document explains how SmartLoan is being built step by step in simple, non-technical language.

SmartLoan is developed like a ladder. Each build stage adds one stronger layer to the product until it becomes a complete loan eligibility and risk assessment system.

---

## Build Stage 1 — Project Foundation

### What was built
The SmartLoan project idea was defined and the basic project structure was created.

### Why it matters
This gave the project a clear starting point, purpose, and direction.

### Outcome
SmartLoan had a proper foundation to begin development.

---

## Build Stage 2 — Customer Journey and Use Cases

### What was built
The customer loan application journey was planned, including what information the applicant provides and how the system should respond.

### Why it matters
This helped connect the project to a real-world lending process.

### Outcome
SmartLoan had clear approval, rejection, and validation scenarios.

---

## Build Stage 3 — First Loan Evaluation Backend

### What was built
The first working backend was created so SmartLoan could receive applicant information and return a loan decision.

### Why it matters
This turned the project from an idea into a working system.

### Outcome
SmartLoan could evaluate one applicant and return an approval or rejection decision.

---

## Build Stage 4 — Requirements and Decision Refinement

### What was built
The required applicant fields, validation rules, risk levels, and decision categories were improved.

### Why it matters
This made the loan decision process clearer and more consistent.

### Outcome
SmartLoan had stronger requirements and better decision structure.

---

## Build Stage 5 — Backend Cleanup and Scoring Review

### What was built
The backend was cleaned and the scoring response was improved with clearer decision information.

### Why it matters
This made the system easier to understand, test, and explain.

### Outcome
SmartLoan returned clearer decisions, risk scores, risk levels, and reasons.

---

## Build Stage 6 — Structured Request and Response Models

### What was built
Structured input and output models were added to control how data enters and leaves the system.

### Why it matters
This helped prevent incorrect or incomplete applicant data from reaching the decision process.

### Outcome
SmartLoan became more reliable and better organised.

---

## Build Stage 7 — Automated Testing

### What was built
Automated tests were added for approval cases, rejection cases, validation errors, and API behaviour.

### Why it matters
This helps confirm that SmartLoan still works correctly after changes are made.

### Outcome
SmartLoan had automated test coverage and stronger reliability.

---

## Build Stage 8 — Database Integration

### What was built
Database storage was added for loan applications and decision results.

### Why it matters
This allowed SmartLoan to keep a history of applications and decisions.

### Outcome
SmartLoan could save and view previous loan application records.

---

## Build Stage 9 — CSV Processing and Data Quality

### What was built
CSV batch processing was added so SmartLoan could evaluate multiple loan applications at once.

### Why it matters
This made the system more useful for bulk processing and data-quality checking.

### Outcome
SmartLoan could process CSV files, detect missing values, detect unrealistic values, and identify duplicate applications.

---

## Build Stage 10 — Synthetic and Mock Data

### What was built
Synthetic applicant data generation was added.

### Why it matters
This allows SmartLoan to be tested safely without using real customer information.

### Outcome
SmartLoan could generate 100 fake loan applicants for testing, CSV processing, and model preparation.

---

## Current Build Position

SmartLoan now has a working backend foundation with validation, scoring, testing, database storage, CSV batch processing, and synthetic data generation.

Each completed build stage adds another layer to the product and prepares SmartLoan for stronger financial analysis, machine-learning risk assessment, explainability, fairness, security, monitoring, deployment, and final product readiness.