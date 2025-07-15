import string

l = [5, 7, 19, 10, 4]

l.append(100)
print(l)
l.remove(7)
print(l)
# ? List can be changed

s = {1, 7, 9}
print(s)

# * Tuples
t = (2, 7, 18, 64, 101, 108, 65)
print(t)

print(t.count(2))
print(t.index(64))
# ? Tuple is unchangeable


l = list(range(10))
print(l)

t = tuple(range(10))
print(t)

# ? List is flexible, but Tuple isn't

print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)

s = string.ascii_letters
print(s)

s = set(s)
print(s)

alpha = tuple(s)
print(alpha)

s = string.ascii_letters
alpha = tuple(list(s))

print(list(s))
print(alpha)

x = 'siddharth#@9563&$QIndiabharat*#(!)Maharashtra pune'

l = list(x)
print(l)

r = []
for c in l:
    if c in alpha:
        r.append(c)

print(r)

print(alpha)
