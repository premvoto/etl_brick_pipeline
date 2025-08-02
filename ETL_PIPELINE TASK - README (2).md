 ETL Brick Pipeline

Automated data pipeline using Azure, Databricks, GitHub Actions, and Python.

#Pipeline Overview

Data Ingestion
-  Python script reads CSV from Azure Blob
-  Databricks notebook transforms data using PySpark and saves to Delta Lake

SQL & Data Validation

- SQL script to check row count
- SQL script to validate unique keys
- SQL script to perform aggregation

CI/CD Setup

- GitHub Actions pipeline triggers on blob upload or file changes
- Run Python unit tests using pytest
- Deploy notebook to Databricks via CLI
- Execute notebook and capture logs

Shell Automation (Bash)

- Schedule pipeline via cron
- Archive logs to Azure Blob
- Trigger workflow via script

Execution Instructions

1. Upload your `.csv` data to Azure Blob Storage.
2. Trigger the workflow via push or scheduled run.
3. Monitor the GitHub Actions workflow logs.
4. Logs and artifacts are archived in Azure Blob container.

Technologies Used

- Azure Blob Storage
- Azure Key Vault
- Databricks (PySpark, SQL)
- GitHub Actions (CI/CD)
- PowerShell & Bash scripting
- Python (pandas, pytest)


