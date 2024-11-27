
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import os
#from sqlalchemy import create_engine
from Extract.Extract_Data import Extract
from Transform.transform_data import Transform_data
from Load.load_data import load_to_mysql

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 1),
    'retries': 1,
}

# Define the DAG
with DAG(
    dag_id='data_pipeline',
    default_args=default_args,
    schedule_interval=None,  # Set to a cron expression for scheduling
    catchup=False,
) as dag:

    # Define Python tasks
    extract_task = PythonOperator(
        task_id='extract',
        python_callable=Extract,
        op_kwargs={'folder_path': '/path/to/data'},  # Update with your folder path
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=Transform_data,
        provide_context=True,
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load_to_mysql,
        provide_context=True,
    )

# Define task dependencies
    extract_task >> transform_task >> load_task
