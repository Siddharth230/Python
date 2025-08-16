def multiply(A,B):
  n = len(A)
  result = [[0 for i in range(n)] for j in range(n)]
  for i in range(n ):
    for j in range(n ):
      for k in range(n):
        result[i][j] += A[i][k] * B[k][j]
  return result


def power(A, m):
    """
    A recursive function to compute A ** m.
    Parameters:
        A: list of lists
        m: integer
    Return:
        result: list of lists
    """
    if m == 1:
      return A
    if m % 2 == 0:
      return multiply(power(A, m // 2),power(A,m // 2))
    else:
      return multiply(A,multiply(power(A,( m - 1) // 2), power(A, ( m - 1) // 2)))
    

l = [[1,2,3],[4,5,6],[7,8,9]]
s = power(l,3)
print(s)