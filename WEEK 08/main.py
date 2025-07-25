"""This program considers an input file and encrypts it by
ceaser cipher. By that we mean, we shift the letters by 3
units. For example, a becomes d, b becomes e and so on ...
w becomes x, x becomes a,y becomes b and z becomes c"""

import string


def create_caeser_dictionary():
    l = string.ascii_lowercase
    l = list(l)
    d = {}
    for i in range(len(l)):
        d[l[i]] = l[(i + 3) % 26]
    return d


f = open("sherlock.txt", "r")
g = open("encrypted_sherlock.txt", "w")

d = create_caeser_dictionary()

c = f.read(1)
while c != "":
    g.write(d[c])
    c = f.read(1)


f.close()
g.close()


# * Now let's decrypt this file


def decryt():
    l = string.ascii_lowercase
    l = list(l)
    d = {}
    for i in range(len(l)):
        d[l[i]] = l[(i - 3 + 26) % 26]
    return d


f = open("encrypte_sherlock.txt", "r")
g = open("decrypt.txt", "w")

a = decryt()
s = f.read(1)
while s != "":
    g.write(a[s])
    s = f.read(1)


f.close()
g.close()
