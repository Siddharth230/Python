
# * Dictionaries

l = [1, 2, 3, 100, 'sid', 'India', 5]
d = {}

d['Siddharth'] = 49329
d['Om'] = 47382
d['Sid'] = 82393

print(d)

print(d['Om'])

print(l)
print(l[0])

# print(d[0])   #? KeyError


malgudi = [
    'It', 'was', 'Monday', 'morning', 'Swaminathan', 'was', 'reluctant', 'to', 'open', 'his', 'eyes', 'he', 'considered', 'Monday', 'specially', 'unpleasant', 'in', 'the', 'calender', 'After', 'the', 'delicious', 'freedom', 'of', 'Saturday', 'and', 'Sunday', 'it', 'was', 'difficult', 'to', 'get', 'into', 'the', 'Monday', 'mood', 'of', 'work', 'and', 'discipline', 'He', 'shuddered', 'at', 'the', 'very', 'thought', 'of', 'school', 'the', 'dismal', 'yellow', 'building', 'the', 'fire', 'eyed', 'Vedanayagam', 'his', 'class', 'teacher', 'and', 'headmaster', 'with', 'his', 'thin', 'long', 'cane']

print(malgudi)

print(len(malgudi))

s = set(malgudi)
print(s)
print(len(s))  # ? Remove duplicates

for x in malgudi:
    print(x)

d = {}

for x in s:
    d[x] = 0


print(s)
print(malgudi)
print(d)

for x in malgudi:
    d[x] += 1

print(d)

max = 0
answer_word = ''

d = {}

for x in s:
    d[x] = 0

print(s)
print(d)

for x in malgudi:
    d[x] += 1
    if d[x] > max:
        max = d[x]
        answer_word = x

print(max)
print(answer_word)

d = {}

d['siddharth'] = [92, 99, 95]
d['om'] = [83, 94, 78]
d['ajit'] = [81, 93, 88]

print(d)

d['siddharth'] = [92, 99, 95, 'siddharth@gmail.com']
d['om'] = [83, 94, 78, 'om@gmail.com']
d['ajit'] = [81, 93, 88, 'ajit@gmail.com']

print(d['siddharth'][0])
print(d['siddharth'][3])
