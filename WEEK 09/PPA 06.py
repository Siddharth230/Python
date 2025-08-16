def spiral_iterative(left, right, n):
    """
    An iterative function to compute the x-coordinate of the nth arm of the spiral.
    Parameters:
        left: integer
        right: integer
        n: integer
    Return:
        result: float
    """
    if n == 0:
      return float(left)
    if n ==1:
      return float(right)
    x_prev = float(left)
    x_curr = float(right)
    for i in range(2, n+1):
      x_next = (x_prev+x_curr)/2.0
      x_prev = x_curr
      x_curr = x_next
    return x_curr


def spiral_recursive(left, right, n):
    """
    An recursive function to compute the x-coordinate of the nth arm of the spiral
    Arguments:
        left: integer
        right: integer
        n: integer
    Return:
        result: float
    """
    if n == 0:
      return float(left)
    if n ==1 :
      return float(right)
    return (spiral_recursive(left,right, n-1) + spiral_recursive(left,right, n-2 ))/2.0
