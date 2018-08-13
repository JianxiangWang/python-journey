# coding: utf-8
from pprint import pprint


class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class TimesFive(MyBaseClass):
    def __init__(self, value):
        super(TimesFive, self).__init__(value)
        self.value *= 5


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        super(PlusTwo, self).__init__(value)
        self.value += 2


class GoodWay(TimesFive, PlusTwo):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)


if __name__ == '__main__':
    foo = GoodWay(5)
    print foo.value
    pprint(GoodWay.mro())  # mro: method resolution order.
