# Jump to Python 문제 - 주어진 인자보다 작은 3과 5의 배수 합을 구하라
def question(arg):
    if not isinstance(arg, int):
        raise TypeError

    result = 0
    for num in range(2, arg):
        if num % 3 == 0 or num % 5 == 0:
            result += num

    return result

result = question(1000)
print(result)