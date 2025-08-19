from typing import List, Optional


class StringManipulation:
    """
    A class to perform various manipulations on a list of words.
    """

    def __init__(self, words: List[str]):
        """
        Initializes the StringManipulation object.

        Args:
            words: A list of lowercase string words.
        """
        self.words = words

    def total_words(self) -> int:
        """
        Returns the total number of words in the list.
        """
        return len(self.words)

    def count(self, some_word: str) -> int:
        """
        Counts the occurrences of a specific word in the list.

        Args:
            some_word: The word to count.

        Returns:
            The number of times some_word appears in the list.
        """
        return self.words.count(some_word)

    def words_of_length(self, length: int) -> List[str]:
        """
        Finds all words of a specific length.

        Args:
            length: The target length of the words.

        Returns:
            A list of words that have the specified length, in their original order.
        """
        return [word for word in self.words if len(word) == length]

    def words_start_with(self, char: str) -> List[str]:
        """
        Finds all words that start with a specific character.

        Args:
            char: The character the words should start with.

        Returns:
            A list of words that start with the given character, in their original order.
        """
        return [word for word in self.words if word.startswith(char)]

    def longest_word(self) -> Optional[str]:
        """
        Finds the longest word in the list.

        If there is a tie in length, the first one encountered in the list is returned.
        Returns None if the list of words is empty.

        Returns:
            The first longest word found in the list.
        """
        if not self.words:
            return None

        return max(self.words, key=len)

    def palindromes(self) -> List[str]:
        """
        Finds all palindromic words in the list.

        A palindrome is a word that reads the same forwards and backwards.

        Returns:
            A list of all palindromes, in their original order.
        """
        return [word for word in self.words if word == word[::-1]]
