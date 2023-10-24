from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

dag = DAG(dag_id='segunda_dag_exemplo',
          description='Minha nova DAG',
          schedule_interval=None,
          start_date=datetime(year=2023, month=4, day=4),
          catchup=False,
          tags=['simples','BashOperator', 'task1 >> [task2, task3]']
          )

task1 = BashOperator(task_id='task_1', bash_command='sleep 5', dag=dag)

task2 = BashOperator(task_id='task_2', bash_command='sleep 5', dag=dag)

task3 = BashOperator(task_id='task_3', bash_command='sleep 5', dag=dag)

task1 >> [task2, task3] # Executes task1 and then executes the task2 and task3 in parallel
