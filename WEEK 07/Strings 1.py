def is_odd_indices_alpha_and_even_indices_digits(string: str) -> bool:
    """
    Given a string, check if all the odd indices are alphabets and the even indices are digits.

    Note: indices starts from 0.

    Arguments:
    string: str - the input string

    Return:
    bool - True if all odd indices are alphabets and even indices are digits, else False
    """
    return all(i.isdigit() for i in string[::2]) and all(
        i.isalpha() for i in string[1::2]
    )


print(is_odd_indices_alpha_and_even_indices_digits("a1b2c3"))
print(is_odd_indices_alpha_and_even_indices_digits("1a2b3c"))

print(is_odd_indices_alpha_and_even_indices_digits("3x4b6d"))
