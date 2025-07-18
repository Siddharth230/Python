
# * Problem 1: Write a Python code using functions which calculates the number of upper case letters, lower case letters, total number of characters and number of words

import math


def upper(s):
    upper = 0
    for c in s:
        if c.isupper():
            upper += 1
    return upper


def lower(s):
    lower = 0
    for c in s:
        if c.islower():
            lower += 1
    return lower


def characters(s):
    chars = 0
    for c in s:
        if c != ' ':
            chars += 1
    return chars


def word(s):
    w = 1
    for c in s:
        if c == ' ':
            w += 1
    return w


sentence = input('Enter the sentence: ')

uLetters = upper(sentence)

lLetters = lower(sentence)

chars = characters(sentence)

words = word(sentence)

print(f'\nTotal number of upper case characters: {uLetters}')

print(f'\nTotal number of lower case characters: {lLetters}')

print(f'\nTotal number of characters: {chars}')

print(f'\nTotal number of words: {words}')


# * Problem 2: Write a Python code using functions to calculate area and perimeter of circle and rectangle

# ? First Approach
shape = input('Enter the shape: ')

output = False

while output != True:
    if shape.lower() == 'circle':
        A = input('What do you want to find? ')
        if A.lower() == 'area':
            r = int(input('Enter radius of circle: '))
            area = 22/7 * (r*r)
            print(f'Area of the Circle is {area}sq. units')
            output = True
        elif A.lower == 'perimeter':
            r = int(input('Enter radius of circle: '))
            perimeter = 2 * (22/7) * r
            print(f'Perimeter of the Circle is {perimeter}units')
            output = True
        else:
            print('Please enter a valid input like area and perimeter')
    elif shape.lower() == 'rectangle':
        A = input('What do you want to find? ')
        if A.lower() == 'area':
            l = int(input('Enter length of the Rectangle: '))
            w = int(input('Enter width of the Rectangle: '))
            area = l*w
            print(f'Area of the Rectangle is {area}sq. units')
            output = True
        elif A.lower == 'perimeter':
            l = int(input('Enter length of the Rectangle: '))
            w = int(input('Enter width of the Rectangle: '))
            perimeter = 2 * (l+w)
            print(f'Perimeter of the Rectangle is {perimeter}units')
            output = True
        else:
            print('Please enter a valid input like area and perimeter')
    elif shape.lower() == 'exit':
        print('Stop execution')
        output = True
    else:
        print('Please enter valid value like circle and rectangle.')


# ? Second Approach

PI = math.pi


def circle_area(r):
    return PI * r*r


def circle_perimeter(r):
    return 2*PI*r


def rectangle_area(l, w):
    return l*w


def rectangle_perimeter(l, w):
    return 2*(l+w)


polygon = ''
while polygon.lower != 'exit':
    print('\nPOLYGONS\ncircle(c)\nrectangle(r)\nexit')
    polygon = input('\nChoose the polygon type or exit: ')
    property = ''
    if polygon.lower() in ('circle', 'c'):
        r = float(input('\nEnter the radius of the circle: '))
        while property == '':
            print('\nCIRCLE PROPERTIES\narea(a)\nperimeter(p)\nback')
            property = input('\nChoose the circle property or go back: ')
            if property.lower() in ('area', 'a'):
                cArea = circle_area(r)
                print(f'\nArea of circle with radius {r} = {cArea} sq.units')
            elif property.lower() in ('perimeter', 'p'):
                cPerimeter = circle_perimeter(r)
                print(
                    f'\nPerimeter of circle with radius {r} = {cPerimeter} units')
            elif property.lower() == 'back':
                break
            else:
                print('Please select the correct polygon property')
                property = ''
    elif polygon.lower() in ('rectangle', 'r'):
        l = float(input('\nEnter the length of the rectangle: '))
        w = float(input('\nEnter the width of the rectangle: '))
        while property == '':
            print('\nRECTANGLE PROPERTIES\narea(a)\nperimeter(p)\nback')
            property = input('\nChoose the rectangle property or go back: ')
            if property.lower() in ('area', 'a'):
                rArea = rectangle_area(l, w)
                print(
                    f'\nArea of rectangle with length {l} and width {w} = {rArea} sq. units')
            elif property.lower() in ('perimeter', 'p'):
                rPerimeter = rectangle_perimeter(l, w)
                print(
                    f'\nPerimeter of rectangle with length {l} and width {w} = {rPerimeter} units')
            elif property.lower() == 'back':
                break
            else:
                print('Please select the correct polygon property')
                property = ''
    elif polygon.lower() == 'exit':
        break
    else:
        print('Please select the correct polygon type or exit')


# * Problem 3: Write a Python code using functions which checks the input coordinates from a triangle or not

# ? First Approach
def distance(xi, yi, xj, yj):
    return (((xj - xi) ** 2) + ((yj-yi) ** 2)) ** 0.5


def isTriangle(m, a, b):
    if a + b > m:
        print('\nTriangle')
    else:
        print('\nNot a triangle')


x1 = float(input('Enter x coordinates of 1st point: '))
y1 = float(input('Enter y coordinates of 1st point: '))
x2 = float(input('\nEnter x coordinates of 2st point: '))
y2 = float(input('Enter y coordinates of 2st point: '))
x3 = float(input('\nEnter x coordinates of 3st point: '))
y3 = float(input('Enter y coordinates of 3st point: '))

d1 = distance(x1, y1, x2, y2)
print(f'\nDistance between points ({x1}, {y1}) and ({x2}, {y2}) = {d1}')

d2 = distance(x2, y2, x3, y3)
print(f'\nDistance between points ({x2}, {y2}) and ({x3}, {y3}) = {d2}')

d3 = distance(x3, y3, x1, y1)
print(f'\nDistance between points ({x3}, {y3}) and ({x1}, {y1}) = {d3}')

if d1 > d2:
    if d1 > d3:
        isTriangle(d1, d2, d3)
    else:
        isTriangle(d3, d1, d2)
elif d2 > d3:
    isTriangle(d2, d1, d3)
else:
    isTriangle(d3, d1, d2)


# ? Second Approach


def slope(xi, yi, xj, yj):
    if (xi == xj):
        return math.inf
    else:
        return (yj-yi) / (xj-xi)


x1 = float(input('Enter x coordinates of 1st point: '))
y1 = float(input('Enter y coordinates of 1st point: '))
x2 = float(input('\nEnter x coordinates of 2st point: '))
y2 = float(input('Enter y coordinates of 2st point: '))
x3 = float(input('\nEnter x coordinates of 3st point: '))
y3 = float(input('Enter y coordinates of 3st point: '))

s1 = slope(x1, y1, x2, y2)
print(
    f'\nSlope of the line connecting points({x1}, {y1}) and ({x2}, {y2}) = {s1}')

s2 = slope(x2, y2, x3, y3)
print(
    f'\nSlope of the line connecting points({x2}, {y2}) and ({x3}, {y3}) = {s2}')

if s1 != s2:
    print('\nTriangle')
else:
    print('\nNot a triangle')
