def extract_lines(filename):
    """
    Get all males who have scored at least 70 marks in Python

    Argument:
        filename: string
    Return:
        None
    """
    f = open(filename, "r")
    w = open("python.csv", "w")

    header = f.readline()
    w.write(header)

    for line in f:
        parts = line.strip().split(",")
        gender = parts[2]
        python_score = int(parts[4])
        if gender == "M" and python_score >= 70:
            w.write(line)
