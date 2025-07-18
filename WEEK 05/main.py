# Find out the minimum most element in the list l
# append that to a new list x
# remove the minimum from the original list l

def min_list(l):
    m = l[0]
    for i in range(len(l)):
        if l[i] < m:
            m = l[i]
    return m


def obv_sort(l):
    x = []
    while len(l) > 0:
        m = min_list(l)
        x.append(m)
        l.remove(m)
    return x


def obvious_sort(l):
    x = []
    while len(l) > 0:
        m = l[0]
        for i in range(len(l)):
            if l[i] < m:
                m = l[i]
        x.append(m)
        l.remove(m)
    return x


List = [4, 39, 68, 9, 17, 1, 53, 28]

print(List)

# print(obvious_sort(List))
print(obv_sort(List))


# We just learnt that braking our problem
# into smaller modules and solving them
# makes it easy
