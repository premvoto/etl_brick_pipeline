Project Overview: End to End ETL Pipeline with CI/CD, Databricks, Automation & Azure Observability

This project demonstrates an end-to-end data engineering pipeline that automates the ingestion, transformation, validation, deployment, and monitoring of data using Databricks, Azure Blob Storage, GitHub Actions, and Azure Log Analytics. The goal was to build a robust, production-ready pipeline with CI/CD integration and secure logging mechanisms.

What I Implemented & Achieved
Data Ingestion & Transformation:
I built a Python-based ingestion script to pull CSV files from Azure Data Lake Storage Gen2. The data is then passed into a Databricks notebook, where I used PySpark to perform data cleaning and transformation. This transformed data is saved in Delta Lake format, which provides ACID compliance and efficient querying.

Data Validation with SQL
Inside Databricks, I implemented SQL-based data validation logic. This includes:
Validating row counts
Checking for unique keys
Aggregating totals like sales by region
These checks ensure the integrity and quality of the ingested data before it's consumed downstream.

CI/CD Pipeline with GitHub Actions
I implemented a fully automated CI/CD pipeline using GitHub Actions defined in ci_pipeline.yml. The pipeline:
Is triggered on code changes, scheduled runs, or manual dispatch
Installs required dependencies and sets up the Python environment
Runs automated unit tests using pytest
Uploads Databricks notebooks via Databricks CLI
Executes remote jobs on Databricks and captures output logs
Archives pipeline logs to Azure Blob Storage
This automation removes the need for manual deployment and ensures reliable delivery of data and code.

Logging & Observability with Azure Log Analytics
To monitor pipeline executions, I created a Python logging system that sends runtime logs to Azure Log Analytics using the Data Collector API. The logs are ingested into a custom table (PipelineLogs_CL) and can be queried using KQL (Kusto Query Language). This provides real-time visibility into pipeline behavior, success/failure events, and execution metrics.

Secure Credential Management
All sensitive information (e.g. Databricks tokens, Azure keys) is stored securely in GitHub Secrets. These are referenced as environment variables in the GitHub Actions workflow. No credentials are exposed in code or logs, ensuring security compliance.

Technologies & Libraries Used
Azure Blob Storage (ADLS Gen2) for storing raw and processed files
Databricks for data processing, transformation, and SQL validation
PySpark for scalable data transformations
GitHub Actions for CI/CD orchestration
Azure Log Analytics for monitoring and log ingestion
requests, hmac, hashlib, base64, datetime in Python for secure log transmission
pytest for unit testing
Databricks CLI for workspace and job automation

Impact & Benefits
Reduced manual operations via full CI/CD automation
Improved data reliability through built-in validation
Secured pipelines with encrypted credential handling
Centralized monitoring through Azure Log Analytics integration
Scalable & reproducible architecture suitable for team collaboration and enterprise usage
