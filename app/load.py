from prefect import task, flow
from app.Task_Class import Task

class DataLoad(Task):

    output_key = 'load_data'
    name = 'load'

    # @task
    def run(self, ro):
        self.logger.info("Data load started")
        data = ro.get('raw_data')
        # ro['load_data'] = data
        return data




