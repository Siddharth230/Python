def number_grid(m, n):
    """
    Write a number grid to a file

    Arguments:
        m, n: positive integers
    Return:
        None
    """
    f = open("numgrid.csv", "w")
    num = 1

    for i in range(m):
        row = [str(num + j) for j in range(n)]
        f.write(",".join(row) + "\n")
        num += n
