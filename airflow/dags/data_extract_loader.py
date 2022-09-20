import os
import sys
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

cwd=os.getcwd()
sys.path.append(f'{cwd}/scripts/')

from extractor import DataExtractor
data_extractor=DataExtractor()

def extract_data(ti):

    loaded_df=data_extractor.extract_data(file_name='20181024_d1_0830_0900.csv')
    # trajectory,vehicle=loaded_df

    ti.xcom_push(key="loaded_df",value=loaded_df)

def create_table():
    pass

def populate_table():
    pass

with DAG(
    dag_id='loader01',
    description='this loads our data to the database',
    start_date=datetime(2022,9,21,3),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='data_loader_task',
        bash_command = "echo task successful!"
    ) 
    
    task2 = BashOperator(
        task_id='data_loader_check_task',
        bash_command = "echo task checked!"
    ) 

    task1.set_downstream(task2)