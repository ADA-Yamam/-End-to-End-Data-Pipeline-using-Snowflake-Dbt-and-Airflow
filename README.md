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
*   `safe_divide`: Prevents division-by-zero errors in calculations
*   ⚠️ Important Technical Notes & Troubleshooting
During the development of this End-to-End pipeline, I handled several critical configuration steps:
Airflow Connections (dbt Cloud API):
To trigger the dbt models, you must obtain your Account ID and Job ID directly from the dbt Cloud URL or Settings.
These IDs must be updated in the dags/dbt_cloud_dag.py file to establish a successful handshake between Airflow and dbt.
Manual dbt Connection Setup:
Note: The dbt connection in Airflow (via Astro/Terminal) does not appear automatically.
You must manually configure the connection in the Airflow UI or via the Terminal using astro dev object create to ensure the orchestrator can "see" your dbt cloud environment.
Finding Airflow Admin Password:
In modern Astro/Docker versions, the default password is not always admin.
Tip: To find your login credentials, go to your Docker Desktop, open the Airflow container logs, and use the search icon to look for "password". It is generated during the first initialization.
Environment Variables:
Ensure all Snowflake credentials are added to a .env file. Refer to .env.example for the required keys.
## ⛓️ How the Integration Works (The Connection)

To achieve a seamless **End-to-End** flow, I integrated the tools as follows:

1.  **Docker (The Container):** Orchestrates the entire environment. It runs **Apache Airflow (Astro)** and ensures all dependencies (like `dbt-snowflake`) are pre-installed via the `Dockerfile`.
2.  **Snowflake (The Warehouse):** Acts as the central data hub. I configured a `profiles.yml` (and `.env` variables) to allow dbt to securely connect and create tables/views.
3.  **dbt (The Transformer):** I built modular SQL models (`staging` & `marts`) and used **Macros** to standardize cleaning logic. All data quality is governed by **4 automated tests** in `schema.yml`.
4.  **Airflow (The Orchestrator):** The Python DAG (`dbt_cloud_dag.py`) acts as the trigger. It communicates with **dbt Cloud API** using a `job_id` and `account_id` to run the transformation models on a daily schedule automatically.


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

 
