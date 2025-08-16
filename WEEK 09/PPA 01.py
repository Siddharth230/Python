def triangular(n):
    """
    Compute the sum of the first n positive integers.
    Parameters:
        n: integer
    Return:
        result: integer
    """
    if n == 1:
      return 1
    else: 
      return n + triangular(n-1)