# n = 10
# ans = 0
# for i in range(n):
#     ans = ans + (i + 1)
# print(ans)


# def sum(n):
#     ans = 0
#     for i in range(n):
#         ans += i + 1
#     return ans


# print(sum(10))
# print(sum(100))


# * Recursion in python
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


# ? Python let's you call the same function within the function
print(sum(10))
print(sum(100))


# ? Compute compound interest by assuming the interest to be 10%
def comp(p, n):
    if n == 1:
        return p * 1.1
    else:
        return comp(p, n - 1) * 1.1


print(comp(1000, 2))


def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n


print(fact(10))
