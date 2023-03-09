from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1)
}

# Define the function to print 'hello' to console
def print_hello():
    print('hello')

# Define the DAG
dag = DAG(
    'print_hello_dag',
    default_args=default_args,
    schedule_interval=None
)

# Define the task to print 'hello'
print_hello_task = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag
)
