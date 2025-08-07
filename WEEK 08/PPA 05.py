def get_matrix(filename):
    """
    Convert the contents of the file into a matrix

    Argument:
        filename: string
    Return:
        matrix: list of lists
    """
    m = []

    f = open(f"{filename}", "r")
    for line in f:
        row = [int(i) for i in line.strip().split(",")]
        m.append(row)

    return m
