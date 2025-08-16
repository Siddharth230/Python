def non_decreasing(L):
    """
    A recursive function that determines if L is sorted in non-decreasing order.
    Parameters: 
        L: list of integers
    Return:
        result: bool
    """
    if len(L) <= 1:
      return True
    if L[0] > L[1]:
      return False
    else:
      return non_decreasing(L[1:])