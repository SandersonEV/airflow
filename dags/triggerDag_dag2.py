from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG(dag_id='dag2__triggered_by_dag1',
         description='Essa é a dag1 triggando a dag2',
         start_date=datetime(year=2022, month=5, day=12),
         schedule_interval=None,
         tags=['BashOperator', '>dag2', 'TriggerDag', 'DagTriggered', 'TriggerDag12'],
         catchup=False
         ) as dag:
    task1 = BashOperator(task_id='task1', bash_command='sleep 5')
