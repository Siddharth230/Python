# * An example of a For loop

n = int(input("Enter a number: "))

for i in range(n):
    if i % 2 == 0:
        print("Hello ", i)
    else:
        print(i, "Hi")
