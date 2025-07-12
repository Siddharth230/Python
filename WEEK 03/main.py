s = 'VIBGYOR'
t = 'VIBGYOR'

# * Example of a Nested For Loop
count = 0
for i in range(7):
    for j in range(7):
        print(i, j, s[i], s[j])
        count += 1


print(
    f"The total ways in which the two brothers can wear 7 different colors: {count}")
