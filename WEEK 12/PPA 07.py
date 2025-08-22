def rotate_list(L, k):
    n = len(L)
    if n == 0:
        return L
    k = k % n
    r = L[-k:] + L[:-k]
    return r


l = list(input().split(","))
k = int(input())

R = rotate_list(l, k)
print(",".join(map(str, R)))
