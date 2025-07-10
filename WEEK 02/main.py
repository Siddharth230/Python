
# * Keywords and Naming rules
roll = 5
Roll = 10
ROLL = 15
print(roll, Roll, ROLL)

# * Multiple assignments
x, y = 1, 2
print(x, y)

a = b = c = 10
print(a, b, c)

x, y = y, x
print(x, y)

# * Deleting a variable

del x  # ? Deletes the variable from memory location

# * Shorthand Operators

#! +=
count = 10
count += 1  # count = count +1
print(count)

#! -=
count = 10
count -= 1
print(count)

#! *=
count = 10
count *= 2
print(count)

#! /=
count = 10
count /= 2
print(count)

#! %=
count = 10
count %= 3
print(count)

# * IN Operator

print("alpha" in "A variable name can only contain alpha-numeric characters and underscores")
print("alpha" in "A variable name must start with a letter or the underscore character")

# * Chaining Operators

x = 5
print(1 < x < 10)
print(10 < x < 20)
print(x < 10 < x*10 < 100)
print(10 > x <= 9)
print(5 == x > 4)
