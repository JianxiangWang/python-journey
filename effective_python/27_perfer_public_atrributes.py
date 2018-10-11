# coding=utf-8


class ParentObject(object):
    def __init__(self):
        self.__private_a = 0


class MyObject(ParentObject):
    def __init__(self):
        super(MyObject, self).__init__()
        self.__private_b = 1


if __name__ == '__main__':
    bar = MyObject()
    print(bar.__dict__)
    print(bar._ParentObject__private_a)