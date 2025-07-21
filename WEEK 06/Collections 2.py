def swap_alternate_elements(t):
    """Swap every alternate of adjacent elements in the tuple.

    Args:
        t (tuple): A tuple of even length.

    Returns:
        tuple: A new tuple with alternate elements swapped.

    Examples:
    >>> swap_alternate_elements((1, 2, 3, 4, 5, 6))
    (2, 1, 4, 3, 6, 5)
    >>> swap_alternate_elements(('a', 'b', 'c', 'd'))
    ('b', 'a', 'd', 'c')
    """
    l_t = list(t)
    for i in range(0, len(l_t) - 1, 2):
        l_t[i], l_t[i + 1] = l_t[i + 1], l_t[i]
    return tuple(l_t)
