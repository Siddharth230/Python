import math
import random as r
from calendar import calendar


print(math.log(10))
print(math.sqrt(225))
print(math.factorial(4))

# print(random.random())  # ? Random number between 0 and 1
print(r.random())

# a = random.random()
a = r.random()

if a < 0.5:
    print('Heads')
else:
    print('Tails')


print(r.randrange(1, 7))


dice1 = r.randrange(1, 7)
dice2 = r.randrange(1, 7)

total = dice1 + dice2

print(f"Rolled dices ({dice1}, {dice2}). Total is {total}")


# print(calendar.month(2025, 6))
# print(calendar.calendar(2025))

print(calendar(2023))
