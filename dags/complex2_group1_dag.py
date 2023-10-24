from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.utils.task_group import TaskGroup

with DAG(dag_id='complex2_group1_dag',
         description='DAG complexa com agrupamento',
         start_date=datetime(year=2023, month=4, day=1),
         catchup=False,
         schedule_interval=None,
         tags=['complex_dag', 'group', 'BashOperator', 'TaskGroup']
         ) as dag:

    task1 = BashOperator(task_id='task_1', bash_command='sleep 2')
    task2 = BashOperator(task_id='task_2', bash_command='sleep 2')
    task3 = BashOperator(task_id='task_3', bash_command='sleep 2')
    task4 = BashOperator(task_id='task_4', bash_command='sleep 2')
    task5 = BashOperator(task_id='task_5', bash_command='sleep 2')
    task6 = BashOperator(task_id='task_6', bash_command='sleep 2')

    task_group = TaskGroup(group_id='task_group', dag=dag)
    task7 = BashOperator(task_id='task_7', bash_command='sleep 2', task_group=task_group)
    task8 = BashOperator(task_id='task_8', bash_command='sleep 2', task_group=task_group)
    task9 = BashOperator(task_id='task_9', bash_command='sleep 2', trigger_rule="one_failed", task_group=task_group)

    task1 >> task2
    task3 >> task4
    [task2, task4] >> task5
    task5 >> task6
    task6 >> task_group
