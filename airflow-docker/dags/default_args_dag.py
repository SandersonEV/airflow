from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow.utils.task_group import TaskGroup

default_args = {
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 15),
    'email_on_failure': False,
    'email': ['san.sev2@gmail.com'],
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
    'owner': "sanderson"
}

with DAG(dag_id='default_args_dag1',
         description='Passando os default_args para as tasks da DAG',
         start_date=datetime(year=2021, month=9, day=15),
         schedule_interval='@hourly',
         default_args=default_args,
         default_view='graph',
         catchup=False,
         tags=['BashOperator', 'default_args']
         ) as dag:
    task1 = BashOperator(task_id='task1', bash_command='sleep 2')
    task2 = BashOperator(task_id='task2', bash_command='sleep 3')
    task3 = BashOperator(task_id='task3', bash_command='sleep 2', retries=3)  # I can rewrite somithing setted in the default_args
    task_group = TaskGroup(group_id='tasks45', dag=dag)
    task4 = BashOperator(task_id='task4', bash_command='sleep 2', task_group=task_group)
    task5 = BashOperator(task_id='task5', bash_command='sleep 5', task_group=task_group)

    task1 >> task2
    task2 >> task_group
    task4 >> task3
