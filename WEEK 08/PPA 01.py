def read_file(filename):
    """
    Read the file and print each line

    Argument:
        filename: string, name of the file to be read
    Return:
        None
    """
    f = open(f"{filename}", "r")
    s = f.read()
    while s != "":
        print(s)
        s = f.read()
