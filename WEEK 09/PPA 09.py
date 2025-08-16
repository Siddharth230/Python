def uniq(L):
    """
    A recursive function to get unique elements from the list.
    Parameters:
        L: list
    Return:
        result: list
    """
    if not L:
      return []
    if L[0] in L[1:]:
      return uniq(L[1:])
    else: 
      return [L[0]] + uniq(L[1:])