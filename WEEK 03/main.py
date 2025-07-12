
# * Break
email = input('Enter an email address: ')
for c in email:
    if c == '@':
        break
    print(c, end='')


# * Continue
email = input('Enter an email address: ')
for c in email:
    if c == '@':
        print('')
        continue
    print(c, end='')


# * pass
for x in range(11):
    if x % 3 == 0:
        print(x)
    else:
        pass
