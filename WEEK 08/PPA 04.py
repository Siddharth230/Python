def get_dict(filename):
    """
    Convert the contents of the file into a dict

    Argument:
        filename: string, path of the file
    Return:
        result: dict; keys are strings, values are integers
    """
    d = {}

    f = open(f"{filename}", "r")
    next(f)
    for line in f:
        name, age = line.strip().split(",")
        d[name] = int(age)

    return d
