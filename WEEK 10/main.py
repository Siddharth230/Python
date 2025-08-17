a = int(input())
b = int(input())
try:
    f = open("abc.txt", "r")
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Invalid input, divisor cannot be zero.")
except NameError:
    print("Variable not defined.")
except FileNotFoundError:
    print("File Not Found.")
except:
    print("Something went wrong.")
finally:
    f.close()
    print("From finally block")


if a < 18:
    raise Exception("You are underage, you cannot vote.")
