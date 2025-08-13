import time


def obvious_search(L, k):
    for x in L:
        if x == k:
            return 1
    return 0


# L = list(range(100000000))
# print(obvious_search(L, 54))


# def sum(n):
#     ans = 0
#     for i in range(n):
#         ans += i
#     return ans


# print(sum(10))
# print(sum(100))

# a = time.time()
# print(sum(10000000))
# b = time.time()
# print(b - a)


# a = time.time()
# print(obvious_search(L, 9999999999))
# b = time.time()
# print("Time taken for Obvious Search ", b - a)


def binary_search(L, k):
    """This function is an alternative for the obvious search.
    It does exactly what is expected from the obvious_search, but in an efficient way.
    This method is popularly called the binary search."""
    begin = 0
    end = len(L) - 1
    while end - begin > 1:
        mid = (begin + end) // 2
        if L[mid] == k:
            return 1
        if L[mid] > k:
            end = mid - 1
        if L[mid] < k:
            begin = mid + 1
    if L[begin] == k or L[end] == k:
        return 1
    else:
        return 0


l = list(range(1000 * 1000 * 1000))

print(len(l))
a = time.time()
print(binary_search(l, -1))
b = time.time()
print("Time taken for Binary Search", b - a)

a = time.time()
print(obvious_search(l, -1))
b = time.time()
print("Time taken for Obvious Search", b - a)
