import numpy as np

def sieve(n: int) -> np.ndarray:
    """Return all primes ≤ n using the Sieve of Eratosthenes."""
    if n < 2:
        return np.array([], dtype=int)

    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False  # 0 and 1 are not primes

    limit = int(n**0.5) + 1
    for i in range(2, limit):
        if sieve[i]:
            sieve[i*i:n+1:i] = False

    return np.flatnonzero(sieve)
