__all__ = ['Struct']

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

    methods_dict = {'__init__': __init__,}

    full_dict = dict(variables_dict, **methods_dict)
    return type('Struct', (object,), full_dict)
