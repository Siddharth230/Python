def f(P):
    mean = sum(P) / len(P)
    return [p - mean for p in P]


def g(P, Q):
    return sum(P[i] * Q[i] for i in range(len(P)))


def h(x):
    return x**0.5


def pearson(X, Y):
    """
        Compute the correlation coefficient
    Arguments:
        X: list of float
        Y: list of float
    Return:
        result: float
    """
    dev_X = f(X)
    dev_Y = f(Y)
    numerator = g(dev_X, dev_Y)
    sum_sq_dev_X = g(dev_X, dev_X)
    sum_sq_dev_Y = g(dev_Y, dev_Y)
    denominator = h(sum_sq_dev_X * sum_sq_dev_Y)
    if denominator == 0:
        return 0.0
    return numerator / denominator


X = [float(x) for x in input().split()]
Y = [float(y) for y in input().split()]
print(f"{pearson(X, Y):.2f}")
