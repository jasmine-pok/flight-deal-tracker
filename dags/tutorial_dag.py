from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_date():
    print(f"Today's date is: {datetime.now()}")

with DAG(
    dag_id='print_date_dag',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['tutorial']
) as dag:

    task_print_date = PythonOperator(
        task_id='print_the_date',
        python_callable=print_date
    )
