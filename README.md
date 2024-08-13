# Kaggle to PostgreSQL Data Pipeline
This project provides a simple pipeline to download datasets from Kaggle, process them, and import them into a PostgreSQL database using Docker.
## Files Overview
- requirements.sh: This shell script installs all the necessary dependencies to run the Python script.
- kaggle-to-postgre.py: A Python script that authenticates with Kaggle, downloads a dataset, processes it, and imports it into a PostgreSQL database.
- runme.sh: A shell script that sequentially executes the requirements.sh script and the kaggle-to-postgre.py script.
## Prerequisites
- Docker and Docker Compose installed on your VPS.
- Python 3.x and pip installed.
- Kaggle account and API key.
- PostgreSQL database running and accessible.
## Setup Instructions
1. Clone the repository:
`git clone <repository-url>`
`cd <repository-folder>`
2. Run the pipeline:
`chmod +x runme.sh`
`./runme.sh`

This script will:
- Install the required libraries using requirements.sh.
- Execute kaggle-to-postgre.py to download the dataset from Kaggle and import it into the PostgreSQL database.
## Configuration
The Python script kaggle-to-postgre.py will prompt you to enter the following information:
1. Kaggle Username: Your Kaggle username for authentication.
2. Kaggle API Key: Your Kaggle API key.
3. Dataset Owner: The owner of the dataset you want to download from Kaggle.
4. Dataset Name: The name of the dataset you wish to download.
5. Data Directory: The directory where the dataset will be saved.
6. PostgreSQL URL: The connection string for your PostgreSQL database (e.g., postgresql://user:password@host:port/dbname).
7. Table Name: The name of the table in which the data will be imported.
## Acknowledgments
1. [Kaggle]('https://www.kaggle.com/') for providing the datasets.
2. [PostgreSQL]('https://www.postgresql.org/') for the database management system.
