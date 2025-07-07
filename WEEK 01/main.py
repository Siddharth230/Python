s = "coffee"
t = "bread"

print(f"s = {s}")
print(f"t = {t}")
print(f"s + t = {s + t}")
print(f"s[0] = {s[0]}")
print(f"s[1:4] = {s[1:4]}")
print(f"s[1:] = {s[1:]}", "\n")

p = '0123456789'
a = p[4]
b = p[7]
c = a + b
print(f"p = {p}", type(p))
print(f"a = p[4] = {a} ", type(a))
print(f"b = p[7] = {b} ", type(b))
print(f"c = a + b = {c}", type(c), "\n")

x = int(p[4])
y = int(p[7])
z = x + y
print(f"x = int(p[4]) = {x} ", type(x))
print(f"y = int(p[7]) = {y} ", type(y))
print(f"z = x + y = {z}", type(z), "\n")

s = "good"
print(f"s = {s}")
print(f"s[0] * 5 = {s[0] * 5}", "\n")

x = "India"
print(f"x = {x}")
print(f"x == 'India' {x == "India"}")
print(f"x == 'india' {x == "india"}", "\n")

print("apple" > "one")
print("four" < "ten")
print("a" < "o")  # Compares letters in alphabetical order
print("cat" > "cap")
print("abcdef" < "abcde")

s = "python"
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])

print(len(s))
