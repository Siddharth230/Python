def add(a, b):
    ans = a+b
    return ans


print(add(1, 6))

print(add(10, 39))


def sub(a, b):
    ans = a-b
    return ans


print(sub(10, 8))


def discount(cost, d):
    ans = cost - (cost*(d/100))
    return ans


print(discount(100, 20))

print(discount(2173, 9))

print(add(17, 5)+sub(100, 3)+discount(1500, 7.5))
