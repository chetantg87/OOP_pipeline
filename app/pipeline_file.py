from app.load import DataLoad
from app.model import Model
from app.preprocess import Preprocess2, Preprocess1
from app import logger
from app.Task_Class import TaskStatus

class Pipeline:

    def __init__(self):
        self.tasks = []
        self.logger = logger
        self.task_status = TaskStatus.PENDING

    def add_task(self, task):
        task.logger = self.logger
        self.tasks.append(task)


    def run(self, ro):
        try:
            for task in self.tasks:
                self.task_status = TaskStatus.RUNNING
                self.logger.info(f'{task.name} is {TaskStatus.RUNNING.name}')
                result = task.run(ro)
                self.task_status = TaskStatus.SUCCESS
                ro[task.output_key] = result
            print(ro)
        except Exception as e:
            self.task_status = TaskStatus.FAILED
            logger.error(str(e))

if __name__=='__main__':

    pipeline = Pipeline()
    ro = dict()
    ro['raw_data'] = [1,2,3,4]
    pipeline.add_task(DataLoad())
    pipeline.add_task(Preprocess1())
    # pipeline.add_task(Preprocess2())
    pipeline.add_task(Model())
    pipeline.run(ro)