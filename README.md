# Web Data Extraction, Transformation, and Loading Pipeline

This project is a complete ETL (Extract, Transform, Load) pipeline built in Python. It automates the process of scraping data from websites, cleaning and transforming the data, and storing it into a MySQL database for further analysis.

---

## **Features**

1. **Data Extraction**
   - Utilizes Python's `selenium` library with WebDriver to scrape data from three websites.
   - Simulates user interactions like scrolling and waiting for elements to load.
   - Saves the extracted data into CSV files for further processing.

2. **Data Transformation**
   - Cleans the data to remove duplicates and inconsistencies.
   - Merges some data into a single file with additional columns for enriched information.

3. **Data Loading**
   - Loads the transformed data into a MySQL database using the `pymysql` library for storage and analysis.

4. **Prefect Pipeline**
   - The entire ETL process is orchestrated using **Prefect**, a modern workflow orchestration framework.
   - Prefect ensures efficient scheduling, monitoring, and error handling of the ETL pipeline.

---

## **Technologies Used**

- **Python**:
  - `selenium`: For web scraping.
  - `pandas`: For data manipulation and transformation.
  - `pymysql`: For database interactions.
  - `prefect`: For workflow orchestration.
- **MySQL**: Database for storing cleaned data.
- **CSV**: Intermediate storage format for raw and cleaned data.

---


4. **Orchestration**:
   - **Prefect** orchestrates the ETL pipeline, ensuring the tasks run sequentially:
     - `Extract`: Fetches the data.
     - `Transform`: Cleans and processes the data.
     - `Load`: Uploads the data to MySQL.
   - Prefect’s features like retries, logging, and monitoring enhance pipeline reliability.

---



