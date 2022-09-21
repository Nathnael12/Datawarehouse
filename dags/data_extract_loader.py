import os
import sys
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

cwd=os.getcwd()
sys.path.append(f'{cwd}/scripts/')
sys.path.append(f'{cwd}/pgsql/')

from extractor import DataExtractor
import db_util

data_extractor=DataExtractor()

def extract_data(ti):

    loaded_df=data_extractor.extract_data(file_name='20181024_d1_0830_0900.csv')
    # trajectory,vehicle=loaded_df
    ti.xcom_push(value=loaded_df)

def create_table():
    db_util.create_table()

def populate_table(ti):
    trajectory_data,vehicle_data = ti.xcom_pull(task_ids='extract_from_file')
    db_util.insert_table(trajectory_data, 'trajectories')
    db_util.insert_table(vehicle_data, 'vehicles')

with DAG(
    dag_id='extractor_loader',
    description='this loads our data to the database',
    start_date=datetime(2022,9,21,3),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='extract_from_file',
        python_callable = extract_data,
    ) 
    
    task2 = PythonOperator(
        task_id='create_table',
        python_callable = create_table
    )
    
    task3 = PythonOperator(
        task_id='load_data',
        python_callable = populate_table
    ) 

    task1.set_downstream(task2)