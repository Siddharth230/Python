def is_palindrome(n: int) -> bool:
    """Checks if an integer is a palindrome.

    Arguments:
    n: int - the integer to check

    Return:
    bool - True if the integer is a palindrome, False otherwise
    """
    a = str(n)
    s = a[::-1]
    return a == s
