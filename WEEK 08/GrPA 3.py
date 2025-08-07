def get_goals(filename, country):
    """
    Get the count of players and their cumulative goals for this country

    Arguments:
        filename: string
        country: string
    Return:
        result: tuple, (integer, integer)
    """
    num_players = 0
    num_goals = 0

    f = open(f"{filename}", "r")
    f.readline()
    for l in f:
        i = l.strip().split(",")
        if len(i) != 3:
            continue
        name, player_country, goals = i
        if player_country == country:
            num_players += 1
            num_goals += int(goals)

    if num_players == 0:
        return (-1, -1)

    return (num_players, num_goals)
