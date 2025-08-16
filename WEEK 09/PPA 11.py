def insert(L, x):
    """
    Insert x in L
    Parameters:
        L: list of sorted integers
        x: integer
    Return:
        result: sorted list of integers
    """
    if not L :
      return [x]
    if x <= L[0]:
      return [x] + L
    else:
      return [L[0]] + insert(L[1:],x)

def isort(L):
    """
    A recursive function to sort the list L
    Arguments:
        L: list of integers
    Return:
        result: sorted list of integers
    """
    if len(L)<=1:
      return L
    return insert(isort(L[1:]),L[0])