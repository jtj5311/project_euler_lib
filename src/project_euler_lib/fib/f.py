from functools import cache


@cache # I guess this isn't so silly and slow w/ caching
def f_slow_and_bad(n: int) -> int:
    # computes the n'th fibonacci (badly)
    # f(0) = 0
    # f(1) = 1 
    # f(n+2) = f(n+1) + f(n)
    
    if n <= 0: return 0
    if n == 1: return 1
    return f_slow_and_bad(n-1) + f_slow_and_bad(n-2)
