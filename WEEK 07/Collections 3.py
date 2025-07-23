def number_of_unique_common_digits(n1: int, n2: int) -> int:
    """
    Given two integers, return the number of unique digits that are common in both numbers.
    Eg, 287498,295424 - 2, 4 and 9 are common to both nums so answer is 3
    Arguments:
    n1: int - the first number
    n2: int - the second number

    Return:
    int - the number of unique common digits.
    """
    d1 = set(str(abs(n1)))
    d2 = set(str(abs(n2)))
    common_digits = d1.intersection(d2)
    return len(common_digits)
