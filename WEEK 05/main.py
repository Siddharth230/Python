def square(limit):
    x = 0
    while x < limit:
        yield x*x
        yield x*x*x
        x += 1


a = square(10)
print(next(a), next(a))
print(next(a), next(a))
print(next(a), next(a))
print(next(a), next(a))
print(next(a), next(a))
print(next(a), next(a))
