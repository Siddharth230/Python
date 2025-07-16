def add(c, a=20, b=30):
    return (a+b-c)


print(add(40, 20, 30))
print(add(a=20, b=30, c=40))
print(add(40))
print(add(40, 10))
print(add(40, 10, 50))
print(add(40, b=10, a=50))
