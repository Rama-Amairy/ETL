from prefect import flow, task

from Extract.Extract_Data import Extract
from Transform.transform_data import Transform_data
from Load.load_data import load_to_mysql

db_config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'port': 3306,
        'database': 'immigration_Law_firms'
            }

@task
def extract_task():
     Extract()

@task
def transform_task():
    Transform_data()

@task
def load_task(db_config):
    load_to_mysql(db_config)

@flow
def data_pipeline(db_config):
    extract_task()
    transform_task()
    load_task(db_config)

if __name__ == "__main__":
   data_pipeline(db_config)