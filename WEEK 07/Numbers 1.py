def seconds_to_minute_seconds(seconds: int) -> tuple:
    """
    Given an integer representing seconds, return a tuple of (minutes, seconds).

    Arguments:
    seconds: int - an integer representing the number of seconds.

    Return: tuple - a tuple of (minutes, remaining_seconds).
    """
    return (seconds // 60, seconds % 60)
