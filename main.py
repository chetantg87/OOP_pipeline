from app.load import DataLoad
from app.model import Model
from app.pipeline_file import Pipeline
from app.preprocess import Preprocess1


if __name__ == "__main__":

    pipeline = Pipeline()
    ro = dict()
    ro['raw_data'] = [1, 2, 3, 4]
    pipeline.add_task(DataLoad())
    pipeline.add_task(Preprocess1())
    # pipeline.add_task(Preprocess2())
    pipeline.add_task(Model())
    pipeline.run(ro)