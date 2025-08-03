End-to-End ETL Pipeline with CI/CD, Databricks & Azure
This project showcases a complete data pipeline built using Databricks, Azure Storage, GitHub Actions, and Log Analytics, focusing on automation, data quality, and observability. The pipeline is built to ingest, transform, validate, deploy, and monitor data with zero manual intervention.

What I Built & Why It Matters:
🔹 Data Ingestion & Processing
Ingested CSV files from Azure Data Lake Storage Gen2 using a Python script.

Processed the data using PySpark in a Databricks notebook and saved it as a Delta Lake table for efficient querying and versioning.

🔹 Data Quality Checks
Wrote SQL queries in Databricks to:
  Check total row count
  Validate primary key uniqueness
  Perform aggregations like sales by region
This ensures reliable, clean data for downstream use.

🔹 CI/CD with GitHub Actions
Set up a CI/CD pipeline using ci_pipeline.yml that:
  Runs on code changes or on a schedule
  Installs dependencies and runs pytest for unit tests
  Uploads notebooks to Databricks using Databricks CLI
  Triggers the notebook job execution
  Archives logs to Azure Blob Storage
This streamlines development, testing, and deployment without manual steps.

🔹 Monitoring with Azure Log Analytics
Created a Python logger to send execution logs to Azure Log Analytics using the Data Collector API.
Logs are stored in a custom table (PipelineLogs_CL) and can be queried with KQL for monitoring pipeline performance and errors.

🔹 Secret & Key Management
All secrets (e.g., tokens, keys) are securely stored in GitHub Secrets.
No sensitive data is hardcoded—values are passed as environment variables in the pipeline.

Tech Stack
  Azure Blob Storage (ADLS Gen2) – raw data storage
  Databricks & PySpark – data transformation
  Databricks SQL – data validation
  GitHub Actions – CI/CD automation
  Azure Log Analytics – log ingestion and monitoring
  Python Packages: requests, pytest, hmac, base64, datetime, json
