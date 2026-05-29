from app.Task_Class import Task
from prefect import task, flow

class Preprocess1(Task):
    output_key = 'pre_process_data1'
    name = 'pre_process'
    # @task
    def run(self, ro: dict):
        self.logger.info("Preprocessing data")
        data =  ro.get('load_data')
        # del ro['load_data']
        data = [x + 1 for x in data]
        # f = 1/0
        # ro['pre_process_data1'] = data
        # print(ro)
        return data
