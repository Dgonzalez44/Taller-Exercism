def square(number):
    if number > 64:
        raise ValueError("Numero muy grande")
    if number < 1:
        raise ValueError("Numero negativo")
    return 2 ** (number - 1)
    pass


def total():
    return 2 ** 64 - 1
    pass
