def get_max_line(filename):
    """
    Get the line that houses the maximum value

    Argument:
        filename: string, path to the file
    Return:
        result: integer
    """
    max_val = 0
    max_line = 0

    f = open(f"{filename}", "r")
    for i, line in enumerate(f, start=1):
        num = int(line.strip())
        if num > max_val:
            max_val = num
            max_line = i

    return max_line
