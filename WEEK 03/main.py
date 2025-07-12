
# * Problem 1: Find all prime numbers less than the entered number

num = int(input('Enter a number: '))

if num >= 2:
    print(2, end=' ')

for i in range(3, num):
    flag = False
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
        else:
            flag = True
    if flag:
        print(i, end=' ')


# * Problem 2: Find the total profit/loss of each trader working in a trading firm. Information regarding number of traders and  number of transactions is unknown

empID = input('Enter employee ID: ')

while empID != '-1':
    trade = int(input('Enter the trade amount: '))
    profit_loss = 0
    while trade != 0:
        profit_loss += trade
        trade = int(input('Enter the trade amount: '))
    print(f'Profit/loss for employee {empID} is {profit_loss}')
    empID = input('\n Enter employee ID: ')


# * Problem 3: Find the day wise total rainfall for the entered duration of time e.g. week, month,etc

days = int(input('Enter the number of days: '))
for i in range(1, days + 1):
    total = 0
    rainfall = int(input('Enter the rainfall: '))
    while rainfall != -1:
        total += rainfall
        rainfall = int(input('Enter the rainfall: '))
    print(f'Total rainfall for the day {i} is {total}')


# * Problem 4: Find the length of longest word from the set of words entered by the user

word = input('Enter a word: ')
maxLen = 0
while word != '-1':
    count = 0
    for letter in word:
        count += 1
    if count > maxLen:
        maxLen = count
    word = input('Enter a word: ')
print(f'The length og longest word is {maxLen}')
