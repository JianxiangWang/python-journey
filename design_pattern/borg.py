# coding: utf-8


class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = "Init"


if __name__ == '__main__':
    pass