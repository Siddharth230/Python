x1 = input()
x2 = input()
y1 = input()
y2 = input()
y3 = input()
z = input()

# swap the values of `x1` and `x2`
x1, x2 = x2, x1

# do a circular swap of `y1`, `y2` and `y3`  like y1 = y2, y2 = y3, y3 = y1
y1, y2, y3 = y2, y3, y1

# create a new variable `a` with the value of `z`
a = z

# delete the variable `z`
del z

print(x1)
print(x2)
print(y1)
print(y2)
print(y3)
# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
print(a)
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task == "sum_until_0":
    total = 0
    n = int(input())
    while n != 0:  # the terminal condition
        total += n  # add n to the total
        n = int(input())  # take the next n form the input
    print(total)

elif task == "total_price":
    total_price = 0
    while True:  # repeat forever since we are breaking inside
        line = input()
        if line == "END":  # The terminal condition
            break
        quantity, price = line.split()  # split uses space by default
        quantity, price = int(quantity), int(price)  # convert to ints
        total_price += quantity * price  # accumulate the total price
    print(total_price)
elif task == "only_ed_or_ing":

    word = input()
    while word.lower() != "stop":
        # both ways of doing it
        if word.lower().endswith("ed") or word.lower()[-3:] == "ing":
            print(word)
        word = input()

elif task == "reverse_sum_palindrome":

    num = int(input())
    while num != -1:
        rev_num = int(str(num)[::-1])
        num_sum = num+rev_num
        if str(num_sum) == str(num_sum)[::-1]:
            print(num)
        num = int(input())

elif task == "double_string":

    line = input()
    while line != "":
        print(line*2)
        line = input()

elif task == "odd_char":

    line = input()
    while line[-1] != ".":
        print(line[::2], end=" ")
        line = input()
    print(line[::2])

elif task == "only_even_squares":

    while True:
        line = input()
        if line == "NAN":
            break
        num = int(line)
        if num % 2 == 0:
            print(num * num)

elif task == "only_odd_lines":

    result = ""
    line_no = 1
    while True:
        line = input()
        if line == "END":
            break
        if line_no % 2:
            result = line + "\n" + result
        line_no += 1
    print(result)
