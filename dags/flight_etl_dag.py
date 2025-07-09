from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# define default arguments
"""default_arg = {
    'owner' : 'airflow',
    'retries' : 1,
    'retry_delay' : timedelta(minutes=5),
    'start_date' : datetime(2025, 6, 1)
}
"""

# define dag
with DAG(
    dag_id='flight_deal_tracker',
    # default_arg=default_arg,
    description='ETL Dag for flight-deal-tracker proj',
    schedule_interval='@daily',
    start_date=datetime(2025, 6, 1),
    catchup=False,
) as dag:
    
    # define wrapper function
    def run_etl():
        try:
            from data_ingestion.auth import get_auth_token
            from data_ingestion.extract import fetch_flight_data
            from data_ingestion.transform import transform_flight_data
            from data_ingestion.load import save_to_csv
            from config.config import ORIGIN, DESTINATION, DEPARTURE_DATE

            token = get_auth_token()
            raw_data = fetch_flight_data(token, ORIGIN, DESTINATION, DEPARTURE_DATE)
            df = transform_flight_data(raw_data)
            save_to_csv(df)

        except ImportError as e:
            print(f"Import error: {e}")
            raise
        except Exception as e:
            print(f"ETL process failed: {e}")
            raise

    # define task using PythonOperator
    etl_task = PythonOperator(
        task_id='run_flight_etl',
        python_callable=run_etl
    )

    


