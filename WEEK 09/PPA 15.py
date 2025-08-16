def subset_sum(L, s):
    """
    A recursive function to determine the presence of a subset with sum s.
    Parameters:
        L: list of integers
        s: integer
    Return:
        result: bool
    """
    if s == 0:
        return True
    if not L:
        return False
    if L[0] <= s:
        if subset_sum(L[1:], s - L[0]):
            return True
    if subset_sum(L[1:], s):
        return True
    return False
