def search(L, k):
    """
    A recursive function that searches for an element k in L.
    Parameters:
      L: list 
      k: int
    Return:
      bool
    """
    if not L:
      return False
    if L[0] == k:
      return True
    else:
      search(L[1:],k)