def most_occuring_first_letter(passage: str) -> str:
    """
    Returns the letter which occurs most frequently
    as the first letter of any word.(case insensitive)

    Args:
        passage (str): A multi-line string representing the passage.

    Returns:
        str: The most frequently occurring first letter in lowercase.
    """
    words = passage.lower().split()
    counts = {}
    for word in words:
        first_letter = word[0]
        counts[first_letter] = counts.get(first_letter, 0) + 1
    return max(counts, key=counts.get)
