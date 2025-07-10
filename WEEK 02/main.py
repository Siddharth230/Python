x = 'pytHoN sTrIng mEthOdS'

print(x.lower())    # ? Converts a string to lower case characters
print(x.upper())    # ? Converts a string to upper case characters
print(x.capitalize())   # ? Converts first characters to upper case
print(x.title())    # ? Converts the first characters of each words to upper case
print(x.swapcase())   # ? Swaps cases, lower case becomes upper case and vice versa


x = 'python'
print(x.islower())  # ? Returns True if all characters in the string are lower case
x = 'Python'
print(x.islower())


x = 'PYTHON'
print(x.isupper())  # ? Returns True if all characters in the string are upper case
x = 'PYTHoN'
print(x.isupper())


x = 'Python String Methods'
print(x.istitle())  # ? Returns True if the string follows the rules of a title
x = 'Python string methods'
print(x.istitle())


x = '123'
print(x.isdigit())  # ? Returns True if all characters in the string are digits
x = '123abc'
print(x.isdigit())


x = 'abc'
print(x.isalpha())
# ? Returns True if all characters in the string are in alphabets
x = 'abc123'
print(x.isalpha())


x = 'abc123ABC'
print(x.isalnum())
# ? Returns True if all characters in the string are alpha-numeric
x = 'abc123@#()'
print(x.isalnum())


x = '-----Python-----'

print(x.strip('-'))  # ? Returns a trimmed version of the string
print(x.lstrip('-'))  # ? Returns a left trim version of the string
print(x.rstrip('-'))  # ? Returns a right trim version of the string


x = 'Python'

print(x.startswith('P'))
# ? Returns True if the string starts with the specified value
print(x.startswith('p'))

print(x.endswith('n'))
# ? Returns True if the string ends with the specifies value
print(x.endswith('N'))


x = 'Python String Methods'

print(x.count('t'))
# ? Returns the number of times a specified value occurs in a string
print(x.count('s'))

print(x.index('t'))
# ? Searches the string for a specified value and returns the position of where it was found
print(x.index('s'))

print(x.replace('S', 's'))
# ? Returns a string where a specified value is replaced with a specified value
print(x.replace('M', 'm'))
