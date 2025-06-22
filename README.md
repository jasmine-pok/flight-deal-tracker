# ✈️ Flight Deal Tracker – Data Engineering Pipeline

This project simulates a production-ready **data engineering pipeline** that automatically fetches, processes, and stores **real-time flight deal data** from the Amadeus API. It showcases ETL orchestration, data transformation, and cloud data warehousing using modern tools and workflows.

## 🚀 Tech Stack

- **Python** – API integration, data cleaning, transformation
- **Apache Airflow** – Workflow scheduling and orchestration
- **dbt (Data Build Tool)** – SQL-based transformations and modeling
- **Google BigQuery** – Cloud data warehouse for analytics and storage
- **pandas** – Data manipulation
- **REST APIs** – Amadeus Flights API

## 🧩 Features

- Authenticates with the Amadeus API and fetches flight offers based on specified parameters (e.g., dates, airports).
- Cleans and normalizes flight deal data using Python.
- Uploads cleaned data to BigQuery for querying and dashboarding.
- Automates ETL workflow using Airflow DAGs.
- Transforms and models raw data into analytics-friendly tables using dbt.

## 🗂️ Project Structure
```plaintext
flight-deal-tracker-Processor/
│
├── dags/ # Airflow DAG definitions
│ └── flight_deals_dag.py
│
├── scripts/
│ ├── fetch_deals.py # Pulls and cleans raw data from Amadeus API
│ └── upload_to_bq.py # Uploads cleaned data to BigQuery
│
├── dbt/
│ ├── models/ # dbt models for transforming data
│ └── dbt_project.yml
│
├── .env # API keys and environment variables (not committed)
├── requirements.txt
└── README.md
```


## 🛠️ Setup & Usage

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/flight-deals-tracker.git
cd flight-deal-tracker
```

### 2. Set up environment variables
#### Create a `.env` file in the root directory and add the following:
```bash
AMADEUS_CLIENT_ID=your_amadeus_api_key
AMADEUS_CLIENT_SECRET=your_amadeus_api_secret
PROJECT_ID=your_gcp_project_id
DATASET_NAME=your_bigquery_dataset
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Locally (Manual Testing)
```bash
python scripts/fetch_deals.py
python scripts/upload_to_bq.py
```

### 5. Schedule with Airflow
Make sure Airflow is installed and properly configured. Then:
- Place the DAG file in your Airflow `dags/` directory.
- Start your Airflow scheduler and webserver to run the pipeline on schedule.

### 6. Run dbt Transformations
Navigate to the `dbt/` directory and run:
```bash
cd dbt/
dbt run
```

## 📊 Example Use Cases
You can use this project to:
- Track airfare trends from specific departure airports
- Build a historical flight deals database for analytics
- Power dashboards using Google Data Studio or Looker on top of BigQuery

## 🧠 Skills Demonstrated 
- API authentication & integration
- ETL pipeline design and data ingestion
- Workflow orchestration using Apache Airflow
- SQL-based data modeling using dbt
- Cloud data warehousing with Google BigQuery
- Automation and pipeline reliability best practices

## 📌 Future Improvements
- Add a Streamlit dashboard to view top deals interactively
- Implement email alerts for flights below a price threshold
- Store historical trends for deeper flight price analysis

## 📄License
This project is for educational and portfolio use only. Commercial use is not permitted.


