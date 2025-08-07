def get_freq(filename):
    """
    Extract frequency information from the file

    Argument:
        filename: string, path to file
    Return:
        result: dictionary; keys are strings, values are integers
    """
    word_count = {}
    f = open(f"{filename}", "r")
    for line in f:
        word = line.strip()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
