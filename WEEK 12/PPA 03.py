def survival(T):
    """
    Determine if the organism will survive or not
    Argument:
        T: integer
    Return:
        result: bool
    """
    for x in range(0, -6, -1):
        for y in range(6):
            t = 30 + (x**2) + (y**2) - (3 * x) - (4 * y)

            if t <= T:
                return True
    return False
