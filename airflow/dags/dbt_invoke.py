

from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# We're hardcoding this value here for the purpose of the demo, but in a production environment this
# would probably come from a config file and/or environment variables!
DBT_PROJECT_DIR = "../../opt/dbt/traffic_data"
DBT_PROFILE_DIR = "../../opt/dbt/"

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['natnaelmasresha@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}    

with DAG(
    "Traffic_dbt_dag",
    start_date=datetime(2022, 9, 20),
    description="DAG that invokes dbt runs",
    schedule_interval=None,
    catchup=False,
    default_args=default_args, 
) as dag:
    
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"dbt run --project-dir {DBT_PROJECT_DIR} --profiles-dir .. ",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"dbt test --project-dir {DBT_PROJECT_DIR} --profiles-dir ..",
    )

    dbt_doc_generate = BashOperator(
        task_id="dbt_doc_gen", 
        bash_command=f"dbt docs generate --project-dir {DBT_PROJECT_DIR} --profiles-dir .. ",

        # bash_command="dbt docs generate --profiles-dir /opt/airflow/dbt --project-dir "
        #               "/opt/airflow/dbt"
    )

dbt_run >> dbt_test >> dbt_doc_generate