
# * Let us find the factorial of a number

n = int(input("Enter a number: "))

i = 1

ans = 1

# ? Executes the loop when condition is True and stops executing when condition becomes False
while i <= n:
    ans *= i
    i += 1


print(ans)
