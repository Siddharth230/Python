def primes_galore(L):
    """
    Compute number of primes located at prime indices
        Argument:
        L: list of integers
    Return:
        result: integer
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_count = 0
    for i, v in enumerate(L):
        if is_prime(i) and is_prime(v):
            prime_count += 1
    return prime_count
