l = [341, 223, 53, 5, 32, 7, 21, 3, 0]


def check0(list):
    for i in range(len(list)):
        if list[i] == 0:
            return True
    return False


print(check0(l))


def Check0(L):
    if len(L) == 0:
        return False
    if L[0] == 0:
        return True
    else:
        return Check0(L[1:])


print(Check0(l))
