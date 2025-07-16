t = 1, 2, 3
print(t, type(t))

x, y, z = t  # ? Unpacking Tuple
print(x, y, z)

x = 5
y = 10
x, y = y, x
print(x, y)

l = [10]
print(l, type(l))

t = (10)
# ? Tuple needs two values for it to be considered as Tuple by Python
print(t, type(t))

t = (10,)
print(t, type(t))

t = ([1, 2], ['a', 'b'])
print(t)

# t[0] = [10, 20]   #* TypeError: 'tuple' object does not support item assignment
# print(t)

t[0][0], t[0][1] = 10, 20  # ? We can modify Lists inside Tuple
print(t)

# * Hashable Tuple
t1 = (1, 2, 3)  # ? Values inside Tuples are immutable

# * Non-Hashable Tuple
t2 = ([1, 2, 3],)  # ? Values inside Tuples are mutable
