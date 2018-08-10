# coding: utf-8

"""
The Borg pattern (also known as the Monostate pattern) is a way to
implement singleton behavior, but instead of having only one instance
of a class, there are multiple instances that share the same state. In
other words, the focus is on sharing state instead of sharing instance
identity.
"""


class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = "Init"

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass


if __name__ == '__main__':
    obj1 = Borg()
    obj2 = Borg()

    print obj1.__dict__
    print obj2.__dict__

    obj1.name = "borg"
    print obj1.__dict__
    print obj2.__dict__

    obj2.state = "obj2"
    print obj1.state

    obj3 = YourBorg()

    print obj1.__dict__
    print obj2.__dict__
    print obj3.__dict__
