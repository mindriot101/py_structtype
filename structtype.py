__all__ = ['Struct']


def __eq__(self, other):
    for name in self.__terms:
        if getattr(self, name) != getattr(other, name):
            return False
    return True


def __len__(self):
    return len(self.__terms)


def Struct(*names):
    variables_dict = {}
    for name in names:
        variables_dict[name] = None

    def __init__(self, *args, **kwargs):
        if len(args) == len(names):
            for (name, value) in zip(names, args):
                self.__dict__[name] = value
        else:
            for name in names:
                self.__dict__[name] = kwargs.get(name, None)

        self.__terms = names

    methods_dict = {'__init__': __init__, '__eq__': __eq__, '__len__': __len__}

    full_dict = dict(variables_dict, **methods_dict)
    return type('Struct', (object,), full_dict)
