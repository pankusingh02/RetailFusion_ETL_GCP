# 🛍️ RetailFusion ETL Platform

A cloud-native, production-grade ETL pipeline that extracts, transforms, and loads retail data from multiple sources (CSV, API, SQL) into **Google BigQuery** for centralized analytics. Built using modular Python scripts and orchestrated with **Apache Airflow**, this pipeline simulates a real-world data engineering workflow deployed in GCP.

---

## 🚀 Features

- Extract data from:
  - 📄 CSV Files (Product Catalogs)
  - 🌐 REST API (Exchange Rates)
  - 🛢️ MySQL Database (Transactional Sales Data)
- Transformations using Pandas:
  - Null handling, timestamp standardization
  - Currency normalization (USD → INR)
  - Daily aggregated metrics (sales per product/category)
- Load data to:
  - 🪣 Google Cloud Storage (as Parquet)
  - 🧠 Google BigQuery (partitioned and clustered tables)
- ⏱️ DAG orchestration with Airflow
- 🔐 Secure secrets with GCP Secret Manager
- 📋 YAML-based config management
- 🐞 Robust logging & error handling

---

## 🧱 Architecture

```plaintext
      +-------------+      +------------------+
      |   CSV File  | ---> |                  |
      |  REST API   | ---> |   Python ETL     | ---> GCS (Staging) ---> BigQuery
      |   MySQL DB  | ---> |  (modular code)  |
      +-------------+      +------------------+
                                |       |
```
---

## ⚙️ Technologies Used
- Language: Python 3.10+
- Data Handling: Pandas, SQLAlchemy, Requests
- Cloud Platform: Google Cloud Platform
- Google Cloud Storage
- Google BigQuery
- Secret Manager
- Workflow Orchestration: Apache Airflow
- Deployment (optional): Docker, GitHub Actions


---

## ✅ Future Enhancements

- Integrate CI/CD via GitHub Actions
- Unit testing using PyTest
- Load metadata & audit logging in BigQuery
-Support streaming data (Kafka / PubSub)
- Looker Studio dashboard on top of BigQuery

---

## 👨‍💻 Author
- Pankaj Singh
- Data Engineer (3+ YOE) | ETL | GCP | Airflow | BigQuery
- 📧 Email: pankajaswal2018@gmail.com

---
