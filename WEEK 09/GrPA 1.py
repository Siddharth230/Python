def reverse(L):
    """
    A recursive function to reverse a list L

    Arguments:
        L: list, type of elements could be anything
    Return:
        result: list
    """
    if len(L) <= 1:
        return L
    return reverse(L[1:]) + L[0]
