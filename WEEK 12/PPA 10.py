def final(n, moves):
    """
    Compute the final position
    Argument:
        n: int
        moves: string
    Return:
        (x, y): tuple
    """
    x, y = 1, 1
    for move in moves:
        if move == "N":
            if y < n:
                y += 1
        elif move == "S":
            if y > 1:
                y -= 1
        elif move == "E":
            if x < n:
                x += 1
        elif move == "W":
            if x > 1:
                x -= 1
    return (x, y)
