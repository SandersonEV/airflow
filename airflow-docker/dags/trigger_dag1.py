from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id='trigger_dag_exemplo',
         description='Minha nova DAG',
         schedule_interval=None,
         start_date=datetime(year=2023, month=5, day=6),
         catchup=False,
         tags=['simples', 'BashOperator', "trigger_rule='one_failed'"]
         ) as dag:

    task1 = BashOperator(task_id='task_1', bash_command='sleep 2')

    task2 = BashOperator(task_id='task_2', bash_command='sleep 2')

    task3 = BashOperator(task_id='task_3', bash_command='sleep 2')

    task4 = BashOperator(task_id='task_4', bash_command='exit 1')

    task5 = BashOperator(task_id='task_5', bash_command='sleep 2')

    task6 = BashOperator(task_id='task_6', bash_command='sleep 2')

    task7 = BashOperator(task_id='task_7', bash_command='sleep 2', trigger_rule="one_failed")

    task1 >> task2 >> task3 >> task4 >> task5 >> task6 >> task7
