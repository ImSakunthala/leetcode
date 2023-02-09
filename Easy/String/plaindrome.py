# ************************************************************
# Given an integer x, return true if x is palindrome integer.
# ************************************************************

def palindrome(x: int):
    result = 0
    number = x
    while number > 0:
        digit = number % 10
        result = 10 * result + digit
        number = number // 10
    if result == x:
        return True
    else:
        return False


x =int(input('x ='))
print (palindrome(x))
