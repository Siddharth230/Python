
# * Concatenation Operators
l1 = [1, 2, 3]
l2 = [10, 20, 30]
l12 = l1 + l2
l21 = l2 + l1
print(l12, l21)


# * Multiplication Operators
l1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(l1)

l2 = [0] * 10
print(l2)

l2 = [1, 2, 3] * 5
print(l2)


# * Logical Operators
l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = [1, 3, 2]
print(l1 == l2)
print(l2 == l3)

print(l2 < l3)

print([1, 2] < [2, 1])
print([1] < [1, 2, 3])
print([2, 3] < [3])
print([] < [3])


l = [1, 2, 4]
print(l)
l[2] = 3
print(l)

s = 'abce'
print(s[3])
# s[3] = 'd'
# print(s)      #? Strings are immutable

x = 5
y = x
x = 10
print(x, y)  # ? Two different memory location for storing values

l1 = [1, 2, 3]
l2 = l1
l1[0] = 100
print(l1, l2)  # ? Both l1 and l2 points to same memory location

l1 = [1, 2, 3]
l2 = list(l1)
l3 = l1[:]
l4 = l1.copy()
l5 = l1

l2[0] = 100
l3[1] = 200
l4[2] = 300

print(l1, l2, l3, l4, l5)

print(l1 is l2)
print(l1 is l3)
print(l1 is l4)
# ? These are variable names associated with different memory location
print(l1 is l5)


def add(x):
    x += 1
    return x


x = 5
print(add(x))  # ? Here we are passing value of the variable
print(x)  # ? Call by Value


def add(y):
    y.append(1)
    return y


y = [5]
print(add(y))  # ? Here we are passing variable itself
print(y)  # ? Call by Reference


l = [1, 2, 3]
print(l)

l.append(4)
print(l)

l.remove(2)
print(l)

x = l.copy()
print(x, l)

l.insert(2, 9)
print(x, l)

l.pop(0)
print(l)


l = [2, 6, 1, 50, 3, 7, 5]
print(l)

l.sort(reverse=True)
print(l)
