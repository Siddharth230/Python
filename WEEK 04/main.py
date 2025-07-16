from math import pi


# squares = []
# for x in range(10):
#     squares.append(x**2)

squares = [x**2 for x in range(10)]
print(squares)


# a = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             a.append((x, y))

a = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(a)


p = [str(round(pi, i)) for i in range(1, 6)]
print(p)


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# A = []
# for i in range(4):
#     A_row = []
#     for row in matrix:
#         A_row.append(row[i])
#     A.append(A_row)

A = [[row[i] for row in matrix] for i in range(4)]
print(A)


B = zip(*matrix)
print(list(B))  # No error if 'list' hasn't been overwritten
