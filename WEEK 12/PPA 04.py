def std_dev(X):
    """
    Compute the standard deviation
    Argument:
        X: list of integers
    Return:
        sigma: float
    """
    n = len(X)
    if n < 2:
        return 0.0
    mean = sum(X) / n

    s2 = sum([(x - mean) ** 2 for x in X])
    v = s2 / (n - 1)
    s = v**0.5
    return s


X = [float(x) for x in input().split(",")]
sigma = std_dev(X)
print(f"{sigma:.2f}")
