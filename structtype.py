def Struct(*names):
    variables_dict = {}
    for name in names:
        variables_dict[name] = None

    full_dict = variables_dict
    return type('Struct', (object, ), full_dict)
