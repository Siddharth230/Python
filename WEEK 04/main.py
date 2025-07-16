# Let us write a few functions on lists

def list_min(l):
    m = l[0]
    for i in range(len(l)):
        if l[i] < m:
            m = l[i]
    return m


def list_max(l):
    m = l[0]
    for i in range(len(l)):
        if l[i] > m:
            m = l[i]
    return m


def list_appendbefore(l, z):
    new_list = []
    for i in range(len(z)):
        new_list.append(z[i])
    for i in range(len(l)):
        new_list.append(l[i])
    return new_list


def list_appendend(l, z):
    for i in range(len(z)):
        l.append(z[i])
    return l


def list_avg(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    avg = sum / len(l)
    return avg


A = [8, 23, 58, 4]
B = [1, 2, 3]

print(list_min(A))
print(list_max(A))
print(list_appendbefore(A, B))
print(list_appendend(A, B))
print(list_avg(A))
