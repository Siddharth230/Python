def sum_of_squares(numbers):
    return sum([n**2 for n in numbers])


def total_cost(cart):
    return sum([q*p for q, p in cart])


def abbreviation(sentence):
    return ".".join([word[0].upper() for word in sentence.split()])+"."


def palindromes(words):
    return [word for word in words if word == word[::-1]]


def all_chars_from_big_words(sentence):
    return {
        l.lower()
        for w in sentence.split()
        for l in w
        if len(w) > 5
    }


def flatten(lol):
    return [e for r in lol for e in r]


def unflatten(items, n_rows):
    n_cols = len(items)//n_rows
    return [
        [items[n_cols*j + i] for i in range(n_cols)]
        for j in range(n_rows)
    ]


def make_identity_matrix(m):
    return [
        [1 if i == j else 0 for i in range(m)]
        for j in range(m)
    ]


def make_lower_triangular_matrix(m):
    return [
        [i+1 if i <= j else 0 for i in range(m)]
        for j in range(m)
    ]
