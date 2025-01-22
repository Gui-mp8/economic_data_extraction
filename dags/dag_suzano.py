from datetime import timedelta
import pendulum

from airflow.decorators import dag
from airflow.models import Variable
from airflow.providers.http.operators.http import HttpOperator

default_args = {
    "owner": "Guilherme Machado Pires",
    "start_date": pendulum.datetime(2024, 4, 26, tz="America/Sao_Paulo"),
    "retries": 0,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    "suzano_desafio",
    default_args=default_args,
    schedule_interval='0 8 * * *',
    # params=config,
    catchup=False,
    tags=["DESAFIO SUZANO"],
)
def suzano():

    invoke_scraper_cloud_run = HttpOperator(
        task_id='invoke_function',
        http_conn_id="scraper_cloud_run_extraction",
        method='GET',
        endpoint='/scraper'
    )

    invoke_scraper_cloud_run
suzano()