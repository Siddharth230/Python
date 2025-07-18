def myFunction1(x):
    x *= 2  # ? Local Variable
    print(f"Value of x in function 1 is {x}")


def myFunction2():
    global x
    x *= 3  # ? Used Existing Global Variable
    print(f"Value of x in function 2 is {x}")


x = 5  # ? Global Variable
print(f"Value of x before function call {x}")

myFunction1(x)

print(f"Value of x after function1 call {x}")

myFunction2()

print(f"Value of x after function2 call {x}")
