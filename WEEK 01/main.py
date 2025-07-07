# Data types

# Integers ( int )
n = 10
print(f"n = {n}")
print("n is of type:", type(n), "\n")


# Float ( float )
r = 6.3
print(f"r = {r}")
print("r is of type:", type(r), "\n")

a = float(9)
print(f"a = {a}")
print(type(a), "\n")


# String ( str )
s = "Siddharth"
print(f"s = {s}")
print("s is of type:", type(s), "\n")


# Boolean ( bool )
b = True
print(b)
print(type(b), "\n")

c = bool(0)
print(c)
print(type(c), "\n")

d = bool(28)
print(d)
print(type(d), "\n")  # All values except 0 are considered as True

e = bool('')
print(e)
print(type(e), "\n")  # Only empty strings are False

f = bool("an31")
print(f)
print(type(f), "\n")


# List ( list )
l = [10, "Siddharth", [1, 2, False], True, 20, 30]
print(l)
print(type(l), "\n")

print(l[0])
print(type(l[0]), "\n")

print(l[1])
print(type(l[1]), "\n")

print(l[2])
print(type(l[2]))
print(type(l[2][1]))
print(l[2][2])
print(type(l[2][2]), "\n")

print(l[3])
print(type(l[3]), "\n")
