def relation(file1, file2):
    """
    Determine the relationship between two files

    Arguments:
        file1, file2: strings, paths to two files
    Return:
        string: 'Equal', 'Subset' or 'No Relation'
    """
    f1 = open(f"{file1}", "r")
    f2 = open(f"{file2}", "r")

    l1 = [i.strip() for i in f1]
    l2 = [i.strip() for i in f2]

    f1_len = len(l1)
    f2_len = len(l2)

    if f1_len == f2_len and l1 == l2:
        return "Equal"

    if f1_len < f2_len and l1 == l2[:f1_len]:
        return "Subset"

    return "No Relation"
