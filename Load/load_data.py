import os
import pandas as pd
import pymysql
from sqlalchemy import create_engine

csv_folder_path="C:/Users/asus/Desktop/Law data/Data/transformed data/"
def read_csv_files_from_folder(folder_path):
    # Initialize an empty dictionary to store DataFrames
    dataframes = {}

    # List all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a CSV file (you can also check for `.csv` extension)
        if file_name.endswith('.csv'):
            # Construct the full file path
            file_path = os.path.join(folder_path, file_name)
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            # Use the file name (without extension) as the dictionary key
            df_name = os.path.splitext(file_name)[0]
            dataframes[df_name] = df

    return dataframes


def load_to_mysql(db_config):
    dataframes = read_csv_files_from_folder(csv_folder_path)
    """
    Load multiple DataFrames into a MySQL database.

    Parameters:
    - dataframes: A dictionary where keys are table names and values are the DataFrames.
    - db_config: A dictionary containing database connection details:
        {
            'user': 'your_username',
            'password': 'your_password',
            'host': 'localhost',
            'port': 3306,
            'database': 'your_database'
        }
    """
    # Create the MySQL connection string
    db_url = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@" \
             f"{db_config['host']}:{db_config['port']}/{db_config['database']}"

    # Create the engine
    engine = create_engine(db_url)

    # Write each DataFrame to a corresponding table
    for table_name, df in dataframes.items():
        print(f"Loading DataFrame into table '{table_name}'...")
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Table '{table_name}' successfully loaded.")

    print("All DataFrames have been loaded to MySQL.")



