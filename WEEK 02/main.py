
# * Problem 1
number = int(input("Enter a number: "))

if (number % 2) == 0:
    print("It is an Even number")
else:
    print("It is an Odd number")


# * Problem 2
num = int(input("Enter a number: "))

if (num % 5) == 0:
    if (num % 10) == 0:
        print('0')
    else:
        print('5')
else:
    print("Other")


# * Problem 3
marks = int(input("Enter students marks: "))

if marks < 0 or marks > 100:
    print('Invalid input: Marks must be between 0 and 100')
elif marks >= 90:
    print('A Grade')
elif marks >= 80:
    print('B Grade')
elif marks >= 70:
    print('C Grade')
elif marks >= 60:
    print('D Grade')
else:
    print('E Grade')


# * Problem 4
time = int(input('Enter time: '))

longer = int(input('Define longer: '))

if time >= longer:
    price = int(input('Enter price: '))
    higher = int(input('Enter higher: '))
    if price >= higher:
        print('Train')
    else:
        print('Coach')
else:
    price = int(input('Enter price: '))
    higher = int(input('Enter higher: '))
    if price >= higher:
        print('Daytime flight')
    else:
        print('Red Eye Flight')


print('Arrive City B')
