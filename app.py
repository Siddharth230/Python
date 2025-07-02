numbers = [3, 5, 4, 7, 9, 10]
max = numbers[0]

for i in numbers:
    if i > max:
        max = i
        print(max)

print(f"Largest number in array is {max}")
