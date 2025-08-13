import time


def obvious_search(L, k):
    for x in L:
        if x == k:
            return 1
    return 0


L = list(range(100000000))
print(obvious_search(L, 54))


def sum(n):
    ans = 0
    for i in range(n):
        ans += i
    return ans


print(sum(10))
print(sum(100))

a = time.time()
print(sum(10000000))
b = time.time()
print(b - a)


a = time.time()
print(obvious_search(L, 9999999999))
b = time.time()
print(b - a)
