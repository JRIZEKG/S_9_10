def greet(name):
    """
    simple greet function, prints hello
    :return: None
    """
    print(f"Hello, {name}")

#greet("Bogdan")
#greet("John")
#greet("Maria")

def special_op(x=10, y=10, z=10):
    """
    Some special operation
    :param x: int or float
    :param y: int or float
    :param z: int or float
    :return: the result of the operation
    """
    return x * y + z

result = special_op(2, 3, 4)
print(result)
print(special_op(2, 3))
print(special_op())
print(special_op(z=2, x=3, y=4))


greet(special_op(2, 3, 4))

def factorial(n):
    """
    Factorial of a number
    :param n: int number
    :return: the value of n!
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

