import sys

class Globe:
    def __setattr__(self, name, value):
        self.__dict__[name] = value

sys.modules[__name__] = Globe