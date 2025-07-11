def is_prime_slow(n:int) -> bool:
    # compute if a number is prime easily
    if n == 2 or n == 3 or n == 5 or n == 7: return True 
    
    i = 1
    i2 = 1
    while i2 <= n:
        if n % i == 0: return False
        
        # (i+1)^2 = i^2 + 2i + 1
        i2 += 2*i + 1
        i += 1

    return True



