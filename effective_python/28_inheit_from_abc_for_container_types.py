# coding=utf-8
from collections.abc import Sequence


class MySequence(Sequence):
    def __init__(self):
        pass

    def __getitem__(self, index):
        pass

    def __len__(self):
        pass


if __name__ == '__main__':
    a = MySequence()