# coding: utf-8
from multiprocessing import Pool


def unwarp_runner_run(args, **kwargs):
    return Runner.run(*args, **kwargs)


class Runner(object):
    def __init__(self):
        pass

    def run(self, a, b):
        return a + b

    def run_multi_thread(self, a_list, b_list):
        inputs = [(self, x, y) for x, y in zip(a_list, b_list)]
        pool = Pool(4)
        res = pool.map(unwarp_runner_run, inputs)
        pool.close()
        pool.join()

        return res


if __name__ == '__main__':
    a_list = range(10)
    b_list = range(10, 20)

    print Runner().run_multi_thread(a_list, b_list)
