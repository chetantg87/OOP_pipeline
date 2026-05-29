from app.Task_Class import Task
from prefect import task, flow

class Model(Task):

    output_key = 'model_data'
    name = 'model'
    # @task
    def run(self, ro: dict):
        self.logger.info("Running model")
        data1 =  ro.get('pre_process_data1')
        # data2 = ro.get('pre_process_data2')
        # data = [*data1, *data2]
        # ro['model_data'] = data1
        # print(ro)
        return data1