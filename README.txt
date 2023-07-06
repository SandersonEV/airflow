__ This readme file will be used to write everthing to help-me to remember of the use of airflow (like a notebook for me) __

Operators:
- BashOperator: executes bash commands
- PythonOperator: executes Python commands
- DummyOperator: Do nothing. is good to organization
- EmailOperator: Sends Email
- SQLOperator: Executes SQL query
- FileSensor: Look if the file is created or modified
- HttpSensor: Wait until the http request be successful
- TriggerDagRunOperator: Start other DAG
- TimeSensor:

Trigger Rules:
- all_success (default): All upstream tasks have succeeded
- all_failed: All upstream tasks are in a failed or upstream_failed state
- all_done: All upstream tasks are done with their execution
- all_skipped: All upstream tasks are in a skipped state
- one_failed: At least one upstream task has failed (does not wait for all upstream tasks to be done)
- one_success: At least one upstream task has succeeded (does not wait for all upstream tasks to be done)
- one_done: At least one upstream task succeeded or failed
- none_failed: All upstream tasks have not failed or upstream_failed - that is, all upstream tasks have succeeded or been skipped
- none_failed_min_one_success: All upstream tasks have not failed or upstream_failed, and at least one upstream task has succeeded.
- none_skipped: No upstream task is in a skipped state - that is, all upstream tasks are in a success, failed, or upstream_failed state
- always: No dependencies at all, run this task at any time

default_args:
- It's used when you're defining a new DAG() and you want to set default arguments to all tasks of this DAG

xcom: To interchange small amounts of data between to tasks
ti(task instance)
    - xcom_push(): set the value
    - xcom_pull(): get the value
