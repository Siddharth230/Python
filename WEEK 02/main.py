alpha = 'abcdefghijklmnopqrstuvwxyz'

name = 'siddharth'

t = ''


for character in name:
    i = alpha.index(character)
    i += 1
    t = t + (alpha[i % 26])


print(t)
