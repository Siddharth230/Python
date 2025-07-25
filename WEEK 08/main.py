f = open("newnum.txt", "r")

flag = 0

s = "0"

while s != "":
    s = f.readline()
    if s != "":
        n = int(s)
        if n == 2:
            print("The number was found")
            flag = 1
            break

if flag == 0:
    print("The number was not found")
