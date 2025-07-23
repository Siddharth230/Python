def has_a_in_second_half(s: str) -> bool:
    """
    Given an even-length string, check if the second half contains
    the character "a" or "A".

    Arguments:
    s: str - an even-length string.

    Return: bool - True if "a" or "A" is found in the second half, else False.
    """
    n = len(s) // 2
    second_half = s[n:]
    return "a" in second_half.lower()


st = "HelloWorld"
print(has_a_in_second_half(st))
