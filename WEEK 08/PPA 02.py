def read_line(filename, n):
    """
    Read the nth line of the file

    Argument:
        filename: string, name of the file to be read
    Return:
        string: return nth line of the file
    """
    f = open(f"{filename}", "r")
    for i in range(n + 1):
        l = f.readline()
        if n <= len(l):
            return l[n - 1].rstrip("\n")
