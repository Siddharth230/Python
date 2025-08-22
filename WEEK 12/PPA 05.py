def balanced(word):
    """
    Determine if a string is balanced
    Argument:
        word: string
    Return:
        result: bool
    """
    stack = []
    m = {"(": ")", "[": "]", "{": "}"}
    for c in word:
        if c in m:
            stack.append(c)
        else:
            if not stack:
                return False
            l = stack.pop()
            if m[l] != c:
                return False
    return not stack
