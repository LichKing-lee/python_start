def sum(*args):
    result = 0
    for number in args:
        result += number

    return result


def multiple(*args):
    result = 1
    for number in args:
        result *= number

    return result
