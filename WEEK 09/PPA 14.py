def minor_matrix(M,i,j):
    return [row[:j] + row[j+1:] for row_index, row in enumerate(M) if row_index != i]

def det(M):
    """
    A recursive function to compute the determinant of M.
    Parameters:
        M: list of lists
    Return:
        result: integer
    """
    if len(M) ==1 :
        return M[0][0]
    if len(M) == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    d = 0
    for j in range(len(M)):
        m = minor_matrix(M,0,j)
        s = (-1) ** j
        d += s * M[0][j] * det(m)
    return d