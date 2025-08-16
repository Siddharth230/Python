def poly(L, x_0):
    """
    A recursive function to compute the value of a polynomial.
    Parameters:
        L: list of integers
        x_0: integer
    Return:
        result: integer
    """
    if not L:
      return 0
    return L[-1] * (x_0 ** (len(L ) -1)) + poly(L[:-1], x_0)