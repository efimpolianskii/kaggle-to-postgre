import os
import pandas as pd
from sqlalchemy import create_engine
import kaggle
import zipfile

def authenticate_kaggle(kaggle_username, kaggle_key):
    """Authenticate with Kaggle API using provided credentials."""
    os.environ['KAGGLE_USERNAME'] = kaggle_username
    os.environ['KAGGLE_KEY'] = kaggle_key
    kaggle.api.authenticate()

def download_dataset(dataset_owner, dataset_name, data_dir):
    """Download dataset from Kaggle."""
    zip_file = os.path.join(data_dir, f'{dataset_name}.zip')
    kaggle.api.dataset_download_files(f'{dataset_owner}/{dataset_name}', path=data_dir, unzip=False)
    return zip_file

def extract_files(zip_file, data_dir):
    """Extract files from the zip archive."""
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(data_dir)

def find_csv_file(data_dir):
    """Find the CSV file in the extracted data."""
    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    if not csv_files:
        raise FileNotFoundError("No CSV files found in the extracted data.")
    return os.path.join(data_dir, csv_files[0])

def load_csv_to_dataframe(csv_file):
    """Load CSV file into a DataFrame."""
    if not os.path.isfile(csv_file):
        raise FileNotFoundError(f"The file {csv_file} does not exist. Please check the file path.")
    return pd.read_csv(csv_file)

def import_data_to_postgres(df, db_url, table_name):
    """Import DataFrame to PostgreSQL database."""
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists='replace', index=False)

def main():
    kaggle_username = input("Enter Kaggle username: ")
    kaggle_key = input("Enter Kaggle API key: ")
    dataset_owner = input("Enter Kaggle dataset owner username: ")
    dataset_name = input("Enter dataset name: ")
    data_dir = input("Enter repository to save the data (ex, 'data'): ")
    db_url = input("Enter PostgreSQL URL for connection (ex, 'postgresql://user:password@host:port/dbname'): ")
    table_name = input("Enter Postgre table name: ")

    authenticate_kaggle(kaggle_username, kaggle_key)
    
    print("Downloading dataset...")
    zip_file = download_dataset(dataset_owner, dataset_name, data_dir)
    
    print("Extracting files...")
    extract_files(zip_file, data_dir)
    
    print("Finding CSV file...")
    csv_file = find_csv_file(data_dir)
    
    print("Loading CSV file into DataFrame...")
    df = load_csv_to_dataframe(csv_file)
    
    print(f"Importing data into table '{table_name}'...")
    import_data_to_postgres(df, db_url, table_name)
    
    print(f"Data successfully imported into the '{table_name}' table in the PostgreSQL database.")

if __name__ == "__main__":
    main()
