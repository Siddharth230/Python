def improvement(filename):
    """
    Find all students who have shown an improvement

    Argument:
        filename: string, path to file
    Return:
        count: integer
    """
    count = 0

    f = open(filename, "r")

    next(f)

    for line in f:
        parts = line.strip().split(",")

        ct = int(parts[2])
        python = int(parts[3])
        pdsa = int(parts[4])

        if ct < python < pdsa:
            count += 1

    return count
