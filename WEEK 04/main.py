import sys

l = list(range(10))

print(l)

l.append('Siddharth')
l.append('India')
l.append(2.71)

print(l)

print(5 in l)
print('Siddharth' in l)
print('siddharth' in l)
print('Om' in l)
print(2.71 in l)
print(2.710 in l)


x = [1, 7, 2, 9, 6, 4, 8, 3, 1]

print(x)

y = {1, 7, 2, 9, 6, 4, 8, 3, 1}

print(type(x))

print(y)
print(type(y))

print(2 in y)
print(10 in y)

s = set(range(100))
print(sys.getsizeof(s))

x = list(range(100))
print(sys.getsizeof(x))
