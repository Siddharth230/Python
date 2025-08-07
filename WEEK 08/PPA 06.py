def write_AP(a_1, d, n):
    """
    Write the AP to a file

    Arguments:
        a_1: first term, integer
        d: common difference, integer
        n: number of terms, integer
    Return:
        None
    """
    f = open("out.txt", "w")
    for i in range(n):
        term = a_1 + i * d
        f.write(str(term) + "\n")
