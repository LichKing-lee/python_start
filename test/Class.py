# no constructor
class Person:
    name = None
    age = None

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def toString(self):
        return "%s은 %s살 입니다." % (self.name, self.age)


person = Person()
person.setName("LichKing")
person.setAge(29)
print(person.toString())


# constructor
class Car:
    tireCount = None
    doorCount = None
    name = None

    def __init__(self, tireCount, doorCount, name):
        self.tireCount = tireCount
        self.doorCount = doorCount
        self.name = name

    def toString(self):
        return "%s의 타이어는 %s개이고, 문은 %s개다." % (self.name, self.tireCount, self.doorCount)


car = Car(4, 4, "어코드")
print(car.toString())


# inherit
class Speakable:
    def speak(self):
        return "Hello World!"


class Singer(Speakable):
    name = None

    def __init__(self, name):
        self.name = name


singer = Singer("naul")
print(singer.speak())
