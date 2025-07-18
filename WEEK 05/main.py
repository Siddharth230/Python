# Initialise C to zero
# Consider two matrices A and B
# Find the dot product of two lists
import numpy


def initialize_mat(dim):
    C = []
    for i in range(dim):
        C.append([])
    for i in range(dim):
        for j in range(dim):
            C[i].append(0)
    return C


def dot_product(u, v):
    dim = len(u)
    ans = 0
    for i in range(dim):
        ans += u[i] * v[i]
    return ans


def row(M, i):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[i][k])
    return l


def col(M, j):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[k][j])
    return l


def mat_mul(A, B):
    dim = len(A)
    C = initialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j] += dot_product(row(A, i), col(B, j))
    return C


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[38, 2, 42], [1, 0, 34], [94, 73, 23]]
print(row(A, 0))
print(col(A, 1))

print(mat_mul(A, B))

A = numpy.asmatrix(A)
B = numpy.asmatrix(B)

C = A*B
print(C)
