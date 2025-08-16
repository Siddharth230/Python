def count(L, word):
    """
    A recursive function to compute the frequency of occurrences of word in L.
    Parameters:
        L: list of words
        word: string
    Return:
        result: integer
    """
    if not L :
      return 0
    if L[0] == word:
      return 1 + count(L[1:],word )
    else:
      return count(L[1:],word)