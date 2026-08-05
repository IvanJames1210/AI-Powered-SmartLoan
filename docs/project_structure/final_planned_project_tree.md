# SmartLoan Final Planned Project Tree

## Document Purpose

This document shows the final planned folder and file structure for the complete SmartLoan project after all 32 build stages.

This is not the current project structure yet. It is the target structure that SmartLoan is being built toward step by step.

The purpose of this document is to help track what already exists, what is still remaining, and how the complete project may look by the final enterprise demo.

---

## Final Planned Project Structure

```text
AI-Powered-SmartLoan/
│
├── backend/
│   │
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── loan_logic.py
│   │   ├── database.py
│   │   ├── csv_processor.py
│   │   ├── synthetic_data_generator.py
│   │   ├── feature_engineering.py
│   │   ├── ml_model.py
│   │   ├── model_evaluation.py
│   │   ├── explainability.py
│   │   ├── fairness.py
│   │   ├── audit_logs.py
│   │   ├── privacy.py
│   │   ├── security.py
│   │   ├── rules_engine.py
│   │   ├── monitoring.py
│   │   ├── config.py
│   │   └── exceptions.py
│   │
│   ├── api/
│   │   ├── loan_routes.py
│   │   ├── csv_routes.py
│   │   ├── application_routes.py
│   │   ├── admin_routes.py
│   │   ├── model_routes.py
│   │   └── monitoring_routes.py
│   │
│   ├── services/
│   │   ├── loan_service.py
│   │   ├── decision_service.py
│   │   ├── csv_service.py
│   │   ├── database_service.py
│   │   ├── feature_service.py
│   │   ├── model_service.py
│   │   ├── audit_service.py
│   │   └── monitoring_service.py
│   │
│   ├── integrations/
│   │   ├── mock_bank_service.py
│   │   ├── mock_credit_bureau_service.py
│   │   ├── mock_employment_service.py
│   │   └── mock_kyc_service.py
│   │
│   ├── ml/
│   │   ├── train_model.py
│   │   ├── predict_model.py
│   │   ├── compare_models.py
│   │   ├── retrain_model.py
│   │   ├── model_registry.py
│   │   └── ml_pipeline.py
│   │
│   ├── tests/
│   │   ├── test_api.py
│   │   ├── test_csv_processing.py
│   │   ├── test_synthetic_data_generator.py
│   │   ├── test_feature_engineering.py
│   │   ├── test_ml_model.py
│   │   ├── test_model_evaluation.py
│   │   ├── test_explainability.py
│   │   ├── test_fairness.py
│   │   ├── test_rules_engine.py
│   │   ├── test_database.py
│   │   ├── test_security.py
│   │   ├── test_integrations.py
│   │   ├── test_monitoring.py
│   │   └── test_performance.py
│   │
│   └── requirements.txt
│
├── frontend/
│   │
│   ├── pages/
│   │   ├── HomePage.jsx
│   │   ├── LoanApplicationPage.jsx
│   │   ├── LoanDecisionResultPage.jsx
│   │   ├── AdminDashboardPage.jsx
│   │   ├── CsvUploadPage.jsx
│   │   ├── ApplicationsHistoryPage.jsx
│   │   └── RiskAnalyticsPage.jsx
│   │
│   ├── components/
│   │   ├── Navbar.jsx
│   │   ├── Sidebar.jsx
│   │   ├── Button.jsx
│   │   ├── InputField.jsx
│   │   ├── SelectField.jsx
│   │   ├── LoanApplicationForm.jsx
│   │   ├── DecisionResultCard.jsx
│   │   ├── RiskScoreCard.jsx
│   │   ├── StatsCard.jsx
│   │   ├── ApplicationsTable.jsx
│   │   ├── CsvUploadBox.jsx
│   │   ├── ChartCard.jsx
│   │   └── LoadingSpinner.jsx
│   │
│   ├── styles/
│   │   ├── global.css
│   │   ├── theme.css
│   │   ├── layout.css
│   │   ├── forms.css
│   │   ├── dashboard.css
│   │   └── responsive.css
│   │
│   ├── api/
│   │   ├── smartLoanApi.js
│   │   ├── loanApplicationApi.js
│   │   ├── csvProcessingApi.js
│   │   └── dashboardApi.js
│   │
│   ├── App.jsx
│   ├── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── data/
│   ├── sample_applications.csv
│   ├── synthetic_applications.csv
│   ├── training_applications.csv
│   ├── testing_applications.csv
│   ├── mock_bank_data.csv
│   ├── mock_credit_bureau_data.csv
│   ├── mock_employment_data.csv
│   └── mock_kyc_data.csv
│
├── models/
│   ├── trained_model.pkl
│   ├── model_metrics.json
│   ├── model_comparison_results.json
│   ├── model_version_history.json
│   └── approved_model.pkl
│
├── migrations/
│   ├── 001_create_loan_applications.sql
│   ├── 002_add_audit_logs.sql
│   ├── 003_add_model_version.sql
│   └── 004_add_monitoring_tables.sql
│
├── docs/
│   ├── 01_business_requirements.md
│   ├── 02_non_technical_build_documentation.md
│   ├── 03_technical_build_documentation.md
│   ├── 04_api_documentation.md
│   ├── 05_database_documentation.md
│   ├── 06_ml_model_documentation.md
│   ├── 07_security_and_privacy_documentation.md
│   ├── 08_testing_documentation.md
│   ├── 09_deployment_documentation.md
│   ├── 10_final_project_summary.md
│   │
│   ├── project_structure/
│   │   └── final_planned_project_tree.md
│   │
│   └── diagrams/
│       ├── 01_project_context.md
│       ├── 02_customer_journey.md
│       ├── 03_use_case_diagram.md
│       ├── 04_api_sequence_diagram.md
│       ├── 05_decision_flow_diagram.md
│       ├── 06_database_erd_diagram.md
│       ├── 07_csv_processing_flow.md
│       ├── 08_synthetic_data_flow.md
│       ├── 09_current_backend_architecture.md
│       ├── 10_final_system_architecture.md
│       ├── 11_ml_pipeline_diagram.md
│       ├── 12_monitoring_dashboard_flow.md
│       └── 13_deployment_and_ci_cd_diagram.md
│
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── .dockerignore
│
├── deployment/
│   ├── cloud_deployment_notes.md
│   ├── environment_variables.md
│   ├── production_readiness_checklist.md
│   └── cost_optimization_notes.md
│
├── mlops/
│   ├── experiment_tracking.md
│   ├── model_registry.md
│   ├── retraining_plan.md
│   └── model_governance.md
│
├── monitoring/
│   ├── monitoring_plan.md
│   ├── api_metrics.md
│   ├── model_performance_metrics.md
│   └── alerting_plan.md
│
├── backup_and_recovery/
│   ├── backup_plan.md
│   ├── recovery_plan.md
│   └── restore_test_notes.md
│
├── demo/
│   ├── demo_script.md
│   ├── demo_video_link.md
│   └── final_enterprise_demo_notes.md
│
├── .github/
│   └── workflows/
│       ├── tests.yml
│       ├── docker-build.yml
│       └── deployment.yml
│
├── README.md
├── TESTING_NOTES.md
├── requirements.txt
├── .gitignore
└── smartloan.db
```

---

## Folder Meaning

```text
backend/                 FastAPI backend, rules, database, ML, security, monitoring
frontend/                Website pages, forms, dashboard, styling, and frontend API calls
data/                    CSV files, synthetic data, mock data, training data, and testing data
models/                  Trained ML models, approved models, and model results
migrations/              Database table changes and upgrades
docs/                    Business, technical, API, testing, deployment, and final documentation
docs/diagrams/           Mermaid diagrams, UML diagrams, ERD, architecture, and ML diagrams
docker/                  Docker setup for containerized running
deployment/              Cloud deployment notes, environment variables, readiness, and cost planning
mlops/                   ML experiment tracking, model registry, retraining, and governance
monitoring/              API monitoring, model monitoring, metrics, and alerting plan
backup_and_recovery/     Backup plan, recovery plan, and restore testing notes
demo/                    Final demo script, demo video link, and enterprise demo notes
.github/workflows/       CI/CD automation using GitHub Actions
README.md                Main project overview
TESTING_NOTES.md         Testing history and test results
requirements.txt         Python dependencies
.gitignore               Files Git should not track
smartloan.db             Local SQLite database file, not normally pushed to GitHub
```

---

## Important Note

This full tree is the final planned structure.

The current SmartLoan project does not contain every file yet. Files and folders should only be created when the correct build stage reaches them.

This keeps the project honest, clean, and easy to explain.