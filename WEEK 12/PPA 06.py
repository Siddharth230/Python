def encrypt_atbash(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    t = str.maketrans(alphabet, reversed_alphabet)
    et = text.translate(t)
    return et
