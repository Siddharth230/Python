
# * Problem 1: Find the factorial of the given number

# ? With While Loop
num = int(input('Enter a number: '))
fact = 1
if num < 0:
    print('Not Defined')
else:
    while num > 0:
        fact *= num
        num -= 1
    print(fact)


# ? With For Loop
num = int(input('Enter a number: '))
fact = 1
if num < 0:
    print('Not defined.')
else:
    for i in range(num, 1, -1):
        fact *= i
    print(fact)


# * Problem 2: Find the number of digits in the given number

# ? With While Loop
num = abs(int(input('Enter a number: ')))
digits = 1
while num > 10:
    num //= 10
    digits += 1
print(digits)


# ? With For Loop
num = abs(int(input('Enter a number: ')))
strNum = str(num)
digits = 0
for c in strNum:
    digits += 1
print(digits)


# * Problem 3: Reverse the digits in the given number

# ? With While Loop
num = int(input('Enter a number: '))
absNum = abs(num)
rev = absNum % 10
absNum //= 10
while absNum > 0:
    r = absNum % 10
    absNum //= 10
    rev = rev * 10 + r
if num > 0:
    print(rev)
else:
    print(rev*-1)


# ? With For Loop
num = int(input('Enter a number: '))
absStrNum = str(abs(num))
rev = ''
for c in absStrNum:
    rev = c + rev
if num >= 0:
    print(rev)
else:
    print('-'+rev)


# * Problem 4: Find whether the entered number is palindrome or not


# ? With While Loop
num = int(input('Enter a number: '))
absNum = abs(num)
rev = absNum % 10
absNum //= 10
while absNum > 0:
    r = absNum % 10
    absNum //= 10
    rev = rev * 10 + r
if num < 0:
    rev *= -1
if rev == num:
    print('Palindrome')
else:
    print('Not a Palindrome')


# ? With For Loop
num = int(input('Enter a number: '))
absStrNum = str(abs(num))
rev = ''
for c in absStrNum:
    rev = c + rev
if num < 0:
    rev = '-' + rev
if num == int(rev):
    print('Palindrome')
else:
    print('Not a Palindrome')
