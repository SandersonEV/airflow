from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

with DAG(dag_id='quarta_dag_exemplo',
         description='Minha nova DAG',
         schedule_interval=None,
         start_date=datetime(year=2023, month=5, day=6),
         catchup=False,
         tags=['simples', 'BashOperator', 'task1 >> task2 >> task3', 'set_upstream', 'with_xxxx_as_xxx:']
         ) as dag:

    task1 = BashOperator(task_id='task_1', bash_command='sleep 5')

    task2 = BashOperator(task_id='task_2', bash_command='sleep 5')

    task3 = BashOperator(task_id='task_3', bash_command='sleep 5')

task1.set_upstream(task2)  # Executes task1 and after task2
task2.set_upstream(task3)

