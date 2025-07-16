s = {1, 2, 3, 4, 5, 1, 2, 3, 5}
print(s)  # ? Sets doesn't allow duplicate values

# print(s[0]) #? Sets are unordered. Sets are not subscriptable

A = {1, 3, 5}
B = {1, 2, 3, 4, 5}
print(A.issubset(B))
print(A.issuperset(B))

C1 = A.union(B)
C2 = A | B  # ? '|' Union Operator
print(C1, C2)

A = {1, 2, 3}
B = {3, 4, 5}
C3 = A.intersection(B)
C4 = A & B  # ? '&' Intersection Operator
print(C3, C4)

C5 = A.difference(B)
C6 = A - B
print(C5, C6)
