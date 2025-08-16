def factorial(n):
    """
    Compute the factorial of n.
    Parameters:
        n: integer
    Return:
        result: integer
    """
    if n == 1:
      return 1
    else: 
      return n * factorial(n-1)