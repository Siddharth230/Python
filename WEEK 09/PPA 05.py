def palindrome(word):
    """
    A recursive function to determine if a string is a palindrome.
    Parameters:
        word: string
    Return:
        result: bool
    """
    if len(word) <=1:
      return True
    if word[0] == word[-1]:
      return palindrome(word[1:-1])
    else:
      return False
