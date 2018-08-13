# coding: utf-8


class ToDictMixin(object):
    """
    A mix-in utility class for converting object to dict.
    """
    def to_dit(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dit()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, v) for v in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


if __name__ == '__main__':

    class Config(ToDictMixin):
        def __init__(self):
            self.lr = 1

    config = Config()
    config.a = "2"
    config.vgg = Config()
    config.vgg.lr = 1
    config.rnn = Config()
    config.rnn.hidden_size = 100

    print config.to_dit()
    print config.__dict__
