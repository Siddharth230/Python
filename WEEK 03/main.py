
# # * Problem 1

# #? First Approach
# n = int(input("Enter a number: "))

# if n < 0:
#     print("Not Defined.")
# else:
#     i = 1
#     fact = 1
#     while i <= n:
#         fact *= i
#         i += 1
#     print(fact)

# # ? Second Approach

# n = int(input('Enter a number: '))
# fact = 1
# if n < 0:
#     print('Not Defined')
# else:
#     while n > 0:
#         fact *= n
#         n -= 1
#     print(fact)


# # * Problem 2

# # ? First Approach

# n = abs(int(input('Enter a number: ')))

# print(len(str(n)))

# # ? Second Approach

# n = abs(int(input('Enter a number: ')))
# digits = 1
# while n > 9:
#     n = n // 10   # ? Removes last digit
#     digits += 1

# print(digits)


# # * Problem 3

# num = int(input('Enter a number: '))
# absNum = abs(num)
# rev = absNum % 10  # ? Extracts last digit
# absNum //= 10  # ? Removes last digit

# while absNum > 0:
#     r = absNum % 10
#     absNum //= 10
#     rev = rev * 10 + r


# if num >= 0:
#     print(rev)
# else:
#     print(rev * -1)


# * Problem 4

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

if num == rev:
    print('Palindrome')
else:
    print('Not a Palindrome')
