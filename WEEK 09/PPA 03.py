def multiply(a, b):
    """
    A recursive function to compute the product of two numbers
    Parameters:
        a, b: integers
    Return:
        result: integer
    """
    if b == 1:
      return a
    else:
      return a + multiply(a,b-1)