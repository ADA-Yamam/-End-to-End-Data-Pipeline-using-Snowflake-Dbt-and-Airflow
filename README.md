# -End-to-End-Data-Pipeline-using-Snowflake-Dbt-and-Airflow
 "A Modern Data Stack (MDS) implementation featuring Snowflake, dbt, Airflow, and Docker. This project demonstrates modular SQL modeling, automated data quality testing via dbt, and reusable logic using Macros (DRY principle) to build a scalable and reliable ELT pipeline."# ❄️ FrostFlow: End-to-End Data Analytics Pipeline

## 📖 Project Overview
This project implements a **Modern Data Stack (MDS)** to automate the lifecycle of retail data. It transforms raw data into actionable business KPIs using a scalable ELT architecture.

---

## 🛠 Tech Stack
*   **Data Warehouse:** Snowflake (Cloud-native scalability)
*   **Transformation:** dbt (Modular SQL & Documentation)
*   **Orchestration:** Apache Airflow (Workflow Management)
*   **Infrastructure:** Docker & Docker-Compose (Containerization)

---

## 🚀 Key Features

### 1. Modular SQL Modeling
The project follows a layered architecture to ensure clean and maintainable code:
*   **Staging Layer:** Standardizing raw data (dates, null handling, trimming).
*   **Mart Layer:** Business logic for Sales KPIs (Revenue, Growth, AOV).

### 2. Advanced Macros (DRY Principle)
Built reusable Jinja/SQL macros to automate repetitive tasks:
*   `clean_string`: Standardizes text columns.
*   `format_money`: Ensures consistent currency formatting.
*   `safe_divide`: Prevents division-by-zero errors in calculations.

### 3. Automated Data Quality (4 Critical Tests)
Integrated automated testing in `schema.yml` to guarantee data integrity:
1.  **Unique:** Ensures no duplicate transactions.
2.  **Not Null:** Guarantees critical fields are always populated.
3.  **Accepted Values:** Validates categorical data.
4.  **Positive Values:** (Custom Test) Ensures financial metrics are always > 0.

---

## 📁 Project Structure
```bash
├── dags/             # Airflow DAGs for orchestration
├── models/           # dbt SQL models (Staging & Marts)
│   ├── staging/      # Raw data cleaning
│   └── marts/        # Business KPIs
├── macros/           # Reusable SQL functions
└── docker-compose.yml # Container configuration

 
