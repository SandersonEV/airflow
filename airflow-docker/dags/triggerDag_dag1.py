from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime

with DAG(dag_id='dag1__trigger_for_dag2',
         description='Essa é a dag1 triggando a dag2',
         start_date=datetime(year=2022, month=5, day=12),
         schedule_interval=None,
         tags=['BashOperator', 'dag1->', 'TriggerDag', 'TriggerDag12'],
         catchup=False,
         default_view='graph',
         ) as dag:

    task1 = BashOperator(task_id='task1', bash_command='sleep 5')
    task2 = TriggerDagRunOperator(task_id='task2', trigger_dag_id='dag2__triggered_by_dag1')

    task1 >> task2
