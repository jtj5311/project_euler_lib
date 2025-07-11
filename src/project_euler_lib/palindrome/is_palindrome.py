from functools import cache


@cache
def is_palindrome(n:int) -> bool:
    str_n = str(n)
    return str_n[::-1] == str_n
