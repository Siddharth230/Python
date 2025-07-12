
for x in range(10):
    print(x, end=' ')

d, m, y = 10, 5, 2021

print("Today's date is", end=' ')
print(d, m, y, sep='/')

num = int(input())

for i in range(1, 11):
    print(num, 'X', i, '=', num*i)
    print(f"{num} X {i} = {num * i}")
    print('{0} X {1} = {2}'.format(num, i, num * i))
    print('%d X %d = %d' % (num, i, num * i))

pi = 22/7
print(f'Value of PI = {pi:.3f}')
print('Value of PI = {0:.9f}'.format(pi))
print('Value of PI = %.0f' % (pi))

print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))
