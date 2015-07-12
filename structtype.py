__all__ = ['Struct']


def __eq__(self, other):
    if sorted(self.members) != sorted(other.members):
        return False

    for name in self.members:
        if getattr(self, name) != getattr(other, name):
            return False
    return True


def __len__(self):
    return len(self.members)


def __iter__(self):
    for name in self.members:
        yield self.__dict__[name]


def __lt__(self, other):
    for name in self.members:
        if getattr(self, name) >= getattr(other, name):
            return False
    return True


def __getitem__(self, name):
    return self.__dict__[name]


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

        self.members = names

    methods_dict = {
        '__init__': __init__,
        '__eq__': __eq__,
        '__len__': __len__,
        '__iter__': __iter__,
        '__lt__': __lt__,
        '__getitem__': __getitem__,
    }

    full_dict = dict(variables_dict, **methods_dict)
    return type('Struct', (object,), full_dict)
