import pandas as pd
from sqlalchemy import create_engine
import os

# Database credentials
DB_USER = 'postgres'
DB_PASSWORD = 'your_password_here'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres' # Default database

# File path
CSV_FILE = 'Nordex_Converter_Data.csv'
TABLE_NAME = 'wind_turbine_data'

def load_data():
    # Check if CSV exists
    if not os.path.exists(CSV_FILE):
        print(f"Error: File {CSV_FILE} not found.")
        return

    print(f"Reading {CSV_FILE}...")
    try:
        df = pd.read_csv(CSV_FILE)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # Convert Timestamp column to datetime objects
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Create SQLAlchemy engine
    connection_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    try:
        engine = create_engine(connection_string)
    except Exception as e:
        print(f"Error creating engine: {e}")
        return

    print(f"Uploading data to table '{TABLE_NAME}'...")
    try:
        # if_exists='append' will append to the table if it exists. 
        # if_exists='replace' would drop the table and recreate it.
        # Using 'append' is safer if table is manually created, but 'replace' is easier for first run.
        # Given the user asked for manual SQL, I'll assume they might create it, so 'append' is good.
        # However, to ensure it works even if they didn't run the SQL, I'll let pandas create it if missing.
        df.to_sql(TABLE_NAME, engine, if_exists='append', index=False)
        print("Data upload successful!")
        
        # Verification
        with engine.connect() as connection:
            result = connection.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
            count = result.fetchone()[0]
            print(f"Total rows in '{TABLE_NAME}': {count}")

    except Exception as e:
        print(f"Error uploading data: {e}")

if __name__ == "__main__":
    load_data()



