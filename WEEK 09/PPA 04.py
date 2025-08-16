def logarithm(x):
    """
    A recursive function to compute the log of x
    Parameters:
        x: integer
    Result:
        result: integer
    """
    if x == 1:
      return 0
    else:
      return 1+ logarithm(x//2)