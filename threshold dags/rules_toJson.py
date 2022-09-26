import json
from datetime import datetime
from airflow.models import DAG
from airflow.operators.python import PythonOperator
  
def get_rules(**context):
    ti = context['ti']
    payload = context["dag_run"].conf
    with open('dags/rules.json', 'w') as f:
        json.dump(payload,f)
        
with DAG(
        dag_id='rules_toJson',
        schedule_interval=None,
        start_date=datetime(2022, 7, 26),
        catchup=False
) as dag:

    # get rules
    task_save_rules = PythonOperator(
        task_id='save_rules',
        python_callable=get_rules,
        provide_context=True
    )

task_save_rules
