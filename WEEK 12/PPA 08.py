def depth(exp):
    """
    Compute the maximum nesting depth
    Argument:
        exp: string
    Return:
        result: integer
    """
    current_depth = 0
    max_depth = 0
    for c in exp:
        if c == "(":
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
        elif c == ")":
            current_depth -= 1
    return max_depth
