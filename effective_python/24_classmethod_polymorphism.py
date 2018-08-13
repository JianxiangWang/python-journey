import os


class GenericInputData(object):

    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    def __init__(self, path):
        super(PathInputData, self).__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config["data_dir"]
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker(object):

    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


def execute(workers):
    pass


def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


class BaseModel(object):
    def build_graph(self):
        raise NotImplementedError


class CNN(BaseModel):
    def __init__(self, config):
        self._config = config

    def build_graph(self):
        pass


class TrainFramework(object):
    def __init__(self, neural_network, config):
        self._neural_network = neural_network
        self._config = config

    def train(self):
        pass


if __name__ == '__main__':

    cnn = CNN("")
    train_framework = TrainFramework(cnn, "")
    train_framework.train()
