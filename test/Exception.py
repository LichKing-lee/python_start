try:
    print("abc" + 12)
except:
    print("catch")

try:
    print("abc" + 12)
except TypeError as error:
    print(error)

# multi exception
def test(*args):
    if len(args) > 5:
        raise ValueError

    else:
        raise TypeError

try:
    test(1, 2)
except ValueError as ve:
    print(ve)
except TypeError as te:
    print(te)

#cumtom exception
class MyException(Exception):
    def __str__(self):
        return "This is Custom Exception"

try:
    raise MyException
except MyException as me:
    print(me)

#finally
try:
    raise MyException
except MyException as me:
    print(me)
finally:
    print("Hello Finally")