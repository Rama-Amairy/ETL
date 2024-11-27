import logging

from Extract.Extract_Data import Extract
from Transform.transform_data import Transform_data
from Load.load_data import load_to_mysql



def main():
    """Main function to orchestrate the data pipeline."""
    try:
        # Define the folder containing the CSV files
        #folder_path = "./data"
        
        # Step 1: Extract
        # 1- firms names work in immigration law in canada (by province)
        #Extract()

    
        # Step 2: Transform
        Transform_data()
        
        # Step 3: Load
        db_config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'port': 3306,
        'database': 'immigration_law_firms'
            }
        
        load_to_mysql(db_config)
        print("Pipeline completed successfully!")
        logging.info("Pipeline completed successfully!")
    except Exception as e:
        logging.error(f"Error during pipeline execution: {e}", exc_info=True)

if __name__ == "__main__":
    main()