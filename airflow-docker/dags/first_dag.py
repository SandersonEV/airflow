from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

dag = DAG(dag_id='primeira_dag_exemplo',
          description='exemplo de dag',
          schedule_interval=None,
          start_date=datetime(year=2023, month=6, day=3),
          catchup=False,  # the catchup tells to execute the past dags even if they weren't executed by the schedule
          tags=['sanderson', 'aprendendo']
          )

task1 = BashOperator(task_id='task_d_1', bash_command='sleep 5', dag=dag)

task2 = BashOperator(task_id='task_d_2', bash_command='echo "oi task 2" ', dag=dag)

task3 = BashOperator(task_id='task_d_3', bash_command='echo "oi task 3"', dag=dag)

task1 >> task2 >> task3
