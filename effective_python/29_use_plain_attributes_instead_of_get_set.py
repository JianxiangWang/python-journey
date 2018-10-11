# coding=utf-8

class Register(object):
    def __init__(self, ohms):
        self.ohms = ohms

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms < 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms


if __name__ == '__main__':
    register = Register(-5)
    register.ohms = -1