# coding=utf-8


class LazyDB(object):
    def __init__(self):
        self.exists = 1

    def __getattr__(self, item):
        pass

