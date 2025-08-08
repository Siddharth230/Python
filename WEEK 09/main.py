def mini(L):
    m = L[0]
    for i in L:
        if i < m:
            m = i
    return m


def Sort(L):
    if L == [] or len(L) == 1:
        return L
    m = mini(L)
    L.remove(m)
    return [m] + Sort(L)


l = [1374, 33, 0, 12, 5, 324]

print(Sort(l))
