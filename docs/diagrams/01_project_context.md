# SmartLoan Diagram 1 — Project Context

```mermaid
flowchart LR
    Applicant[Loan Applicant] --> SmartLoan[SmartLoan Eligibility and Risk Engine]
    Business[Lender / Fintech Business] --> SmartLoan
    SmartLoan --> Decision[Loan Decision: Approved or Rejected]
    SmartLoan --> Risk[Risk Score, Risk Level, and Reasons]
    SmartLoan --> Storage[(Application and Decision History)]
```