from datetime import datetime

from airflow.decorators import dag, task


@dag(schedule='@once', start_date=datetime(2022, 1, 1), catchup=False)
def tacticvis_pipeline():
    @task()
    def extract():
        print("Extracting data")

        data = {
            "col1": [1, 2, 3],
        }
        return data

    @task()
    def transform(data):
        print("Transforming data")
        return data

    @task()
    def load(data):
        print("Loading data")
        print(data)

    match_data = extract()
    transformed_data = transform(match_data)
    load(transformed_data)


tacticvis_pipeline_dag = tacticvis_pipeline()
