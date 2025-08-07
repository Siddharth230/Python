def add_period(filename):
    """
    Add a period at the end of each line

    Argument:
        filename: string; path of the file
    Return:
        None
    """
    f = open(filename, "r")
    w = open("out.txt", "w")

    for line in f:
        line = line.rstrip("\n")
        w.write(line + "." + "\n")
