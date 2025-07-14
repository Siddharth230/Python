
l = [1, 7, 4, 2, 100]

print(l)

l.append(1024)
print(l)

l.append(2)
print(l)

l.remove(1)
print(l)

l.remove(2)  # ? Removes first occurrence
print(l)

x = []

x.append(l)
print(x)

m = [10, 20, 30]

x.append(m)
print(x)

t = []

t.append(x)
print(t)

t.append([100, 101, 102])
print(t)

print(t[0])
print(t[1])

M = []

M.append([1, 2, 3])
M.append([4, 5, 6])
M.append([7, 8, 9])

print(M)
