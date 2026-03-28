from airflow import DAG
from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator
from datetime import datetime, timedelta

# 1. Task Default Arguments (Best Practices)
default_args = {
    'owner': 'Analytics_Engineer',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
                        
}

# 2. DAG Definition (The Maestro)
with DAG(
    dag_id='dbt_snowflake_weekly_production',
    default_args=default_args,
    description='Professional Pipeline to trigger dbt Cloud Transformations in Snowflake',
    schedule='0 9 * * 1', # Every Monday at 9:00 AM
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=['dbt_cloud', 'snowflake', 'north_america_us1'],
) as dag:

    # 3. Main Task: Trigger dbt Cloud Job
    # Configured for North America Multi-cell (us1) infrastructure
    run_dbt_job = DbtCloudRunJobOperator(
        task_id='trigger_dbt_build_job',
        dbt_cloud_conn_id='dbt_cloud_default',
        account_id=70471823545182, 
        job_id=70471823576688,      
        check_interval=30,          
        timeout=3600,               
        wait_for_termination=True,  
        deferrable=False, # Set to False for better stability in Docker environments
        # Mandatory for us1 servers to bypass 406 Not Acceptable error
        additional_run_config={"cause": "Automated Airflow Pipeline Trigger"}
    )

    run_dbt_job
