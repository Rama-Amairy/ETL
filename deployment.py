from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import IntervalSchedule
from datetime import timedelta
from data_pipeline import data_pipeline  # Replace `your_script` with the actual script name

# Define schedule
schedule = IntervalSchedule(interval=timedelta(hours=24))  # Runs every 24 hours

# Create deployment
deployment = Deployment.build_from_flow(
    flow=data_pipeline,
    name="Daily ETL Pipeline",
    parameters={"db_config": {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'port': 3306,
        'database': 'immigration_Law_firms'
    }},
    schedule=schedule,
)

if __name__ == "__main__":
    deployment.apply()
