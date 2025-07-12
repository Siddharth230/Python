
# * Adds the first 10 integers

n = int(input("Enter a number: "))

ans = 0

for i in range(n+1):
    ans += i


print(f"The summation of all the numbers until {n} is {ans}.")
