min = None


def find_min(items: list):
    m = items[0]
    for i in items[1:]:
        if i < m:
            m = i
    return m


def odd_increment_even_decrement_no_modify(items) -> list:
    new_items = []
    for i in items:
        if i % 2 != 0:
            new_items.append(i+1)
        else:
            new_items.append(i-1)
    return new_items


def odd_square_even_double_modify(items: list) -> list:
    for i in range(len(items)):
        if items[i] % 2 != 0:
            items[i] **= 2
        else:
            items[i] *= 2
    return items


def more_than_two_unique_vowels(sentence):
    vowels = set('aeiou')
    words = set()
    for w in sentence.split(","):
        if len(set(w) & vowels) > 2:
            words.add(w)
    return words


def sum_of_list_of_lists(lol):
    total = 0
    for r in lol:
        for i in r:
            total += i
    return total


def flatten(lol):
    flat = []
    for r in lol:
        for i in r:
            flat.append(i)
    return flat


def all_common(strings):
    common_chars = set(strings[0])
    for s in strings[1:]:
        common_chars &= set(s)
    return ''.join(sorted(common_chars))


def vocabulary(sentences):
    vocab = set()
    for s in sentences:
        for word in s.split(" "):
            vocab.add(word.lower())
    return vocab
