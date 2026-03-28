from airflow import DAG
from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator
from datetime import datetime, timedelta

# 1. Task Default Arguments (Best Practices)
# These settings ensure the pipeline is robust and handles retries automatically
default_args = {
    'owner': 'Analytics_Engineer',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5), # Standard delay for cloud triggers
}

# 2. DAG Definition (The Maestro)
# This orchestrator schedules the dbt transformation workflow
with DAG(
    dag_id='dbt_snowflake_weekly_production',
    default_args=default_args,
    description='Professional Pipeline to trigger dbt Cloud Transformations in Snowflake',
    schedule='0 9 * * 1', # Every Monday at 9:00 AM
    start_date=datetime(2024, 1, 1), # Standard historical start date
    catchup=False,
    tags=['dbt_cloud', 'snowflake', 'production', 'automated'],
) as dag:

    # 3. Main Task: Trigger dbt Cloud Job
    # This task sends an API request to dbt Cloud to start the modeling process
    run_dbt_job = DbtCloudRunJobOperator(
        task_id='trigger_dbt_build_job',
        dbt_cloud_conn_id='dbt_cloud_default', # Must be configured manually in Airflow UI
        account_id=000000,           # Replace with your actual dbt Cloud Account ID
        job_id=000000,               # Replace with your actual dbt Cloud Job ID
        check_interval=60,           # Polling frequency (seconds)
        timeout=3600,                # 1-hour timeout limit
        wait_for_termination=True,   # Wait for the dbt job to finish before completing task
        deferrable=False,            # Set to False for higher stability in local Docker setups
        
        # Mandatory configuration for North America (us1) infrastructure 
        # to ensure compatibility and bypass 406 Not Acceptable errors
        additional_run_config={"cause": "Automated Airflow Pipeline Trigger via GitHub Repo"}
    )

    # Note: Dependencies can be added here if the pipeline grows
    run_dbt_job
