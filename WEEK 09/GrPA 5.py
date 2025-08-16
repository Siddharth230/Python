def ancestry(P, present, past):
    """
    A recursive function to compute the sequence of ancestors of person

    Arguments:
        P: dict, key and value are strings
        present: string
        past: string
    Return:
        result: list of strings
    """
    if present == past:
        return [present]
    father = P[present]
    return [present] + ancestry(P, father, past)
