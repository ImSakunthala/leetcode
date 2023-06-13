" lambda function : To create anonymous function Take any number of arguments but can have any expression."


def exp(n):
    return lambda a: a * n


expo = exp(2)
print(expo(11))

"filter function: allows you to process an iterable and extract those items that satisfy a given condition"


def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


filtered = filter(isprime, range(10))
print(list(filtered))


"map function: Map in Python is a function that works as an iterator to return a result after applying a function " \
"to every item of an iterable (tuple, lists, etc.). It is used when you want to apply a single transformation " \
"function to all the iterable elements.The iterable and function are passed as arguments to the map in Python."


def cube(n):
    return n*n*n


print(list(map(cube, [1, 2, 3, 4, 5])))