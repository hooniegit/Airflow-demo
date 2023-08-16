from datetime import datetime, timedelta
import pendulum

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator

local_tz = pendulum.timezone('Asia/Seoul')

# 프로젝트의 모든 DAG 공통 사항 기재
default_args = {
    "owner" : "OppenheimerJoa",
    "depends_on_past" : True,
    "retries" : 1,
    "retry_delay" : timedelta(minutes=1)
}

# 프로젝트마다 변동될 DAG 사항들 기재
dag = DAG(
    dag_id='extract.TMDB.movies.lists.test',
    description='extract movies lists and save JSON file',
    tags=['exaple', 'start', 'todo'],
    max_active_runs=1, # 동시에 실행되는 DAG의 수
    concurrency=1, # 동시에 실행되는 작업의 수
    start_date=datetime(year=2023, month=8, day=7, hour=0, minute=0, tzinfo=local_tz),
    schedule_interval='*/30 * * * *',
    user_defined_macros={},
    default_args=default_args
)

start = EmptyOperator(
    task_id="start",
    dag=dag
)

HOME_DIR = "/Users/kimdohoon/git/hooniegit/Airflow-demo/v2.0.0"
year = 2021

# 디렉토리 수정 필요
# extract = BashOperator(
#     task_id="extract",
#     bash_command=f"""
#     python3 {HOME_DIR}/src/TMDB/extract/extract.py {year}
#     """,
#     dag=dag
# )

extract_II = BashOperator(
    task_id="extract.II",
    bash_command=f"""
    python3 {HOME_DIR}/src/TMDB/extract/extract_after.py {year} 500
    """,
    dag=dag
)

extract_III = BashOperator(
    task_id="extract.III",
    bash_command=f"""
    python3 {HOME_DIR}/src/TMDB/extract/extract_after.py {year} 1000
    """,
    dag=dag
)

extract_IV = BashOperator(
    task_id="extract.IV",
    bash_command=f"""
    python3 {HOME_DIR}/src/TMDB/extract/extract_after.py {year} 1500
    """,
    dag=dag
)

extract_V = BashOperator(
    task_id="extract.V",
    bash_command=f"""
    python3 {HOME_DIR}/src/TMDB/extract/extract_after.py {year} 2000
    """,
    dag=dag
)

extract_VI = BashOperator(
    task_id="extract.VI",
    bash_command=f"""
    python3 {HOME_DIR}/src/TMDB/extract/extract_after.py {year} 2500
    """,
    dag=dag
)

clensing = BashOperator(
    task_id="clensing",
    bash_command=f"""
    echo "Hello, World!"
    """,
    dag=dag
)

end = EmptyOperator(
    task_id="end",
    dag=dag
)

# start >> extract >> extract_II >> extract_III >> extract_IV >> extract_V >> extract_VI >> clensing >> end
start >> extract_II >> extract_III >> extract_IV >> extract_V >> extract_VI >> clensing >> end