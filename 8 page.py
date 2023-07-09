"""
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1

a = Counter()
print(a.count)
a.increment()
print(a.count)
"""

"""
class Counter:
    def __init__(self, initValue = 0): #초기값 설정
        self.count = initValue

a = Counter(100)
b = Counter()
print(a.count, b.count)
"""

"""
class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
    
    def show(self):
        print(self.channel, self.volume, self.on)
    
    def setChannel(self, channel):
        self.channel = channel
    
    def getChannel(self):
        return self.channel
    
t = Television(9,10,True)
t.show()
t.setChannel(11)
t.show()
"""

"""
from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def getArea(self):
        return pi*(self.radius)**2
    
    def getPrimeter(self):
        return 2*pi*self.radius

a = Circle(10)
print("원의 면적 = ", a.getArea())
print("원의 둘레 = ",a.getPrimeter())
"""

"""
class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
    
    def drive(self):
        self.speed = 60

myCar = Car(0,"blue","E-class")
print("자동차 속도는", myCar.speed)
print("자동차 색상은", myCar.color)
print("자동차 모델은", myCar.model)
myCar.drive()
print("자동차 속도는", myCar.speed)
"""

"""
class Student:
    def __init__(self, name = None, age = 0):
        self.__name = name
        self.__age = age

obj = Student
print(obj.__name) #정보 은닉해서 안보임
"""

"""
class Student:
    def __init__(self, name = None, age = 0):
        self.__name = name
        self.__age = age

    def getAge(self):
        return self.__age
    
    def getName(self):
        return self.__name
    
    def setAge(self,age):
        self.age = age

    def setName(self,name):
        self.name = name

obj = Student("Hong", 20)
print(obj.getName())
"""

"""
class Bank:
    def __init__(self):
        self.__balance = 0
    
    def withdraw(self, amount):
        self.__balance -= amount
        print("통장에", amount,"가 출금되었음")
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        print("통장에", amount, "가 입금되었음")
        return self.__balance

a = Bank()
a.deposit(1000)
a.withdraw(10)
"""

"""
class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
    
    def show(self):
        print(self.channel, self.volume, self.on)
    
    def setChannel(self, channel):
        self.channel = channel
    
    def getChannel(self):
        return self.channel
    
t = Television(9,10,True)
s = t

s.setChannel(100)
t.show() #s를 바꿔도 t도 바뀜

if s == t:
    print("2개의 변수는 동일한 객체를 참조하고 있습니다.")
else:
    print("아닙니다.")
"""

"""
class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

    def show(self):
        print(self.channel, self.volume, self.on)

def setSilentMode(t): #클래스를 함수로 전달 가능
    t.volume = 2

myTv = Television(11, 10 ,True)
setSilentMode(myTv)
myTv.show()
"""

"""
class Television:
    serialNumber = 0  #클래스 변수는 클래스당 하나만 생성되어 모든 객체가 이것을 공유합니다.

    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
        Television.serialNumber += 1
        self.number = Television.serialNumber

    def show(self):
        print(self.channel, self.volume, self.on, self.number)

myTv = Television(11,10,True)
myTv.show()
"""

"""
class Monster:
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERYSTRONG = 30

    def __init__(self):
        self.__health = Monster.NORMAL
    
    def eat(self):
        self.__health = Monster.STRONG
    
    def attack(self):
        self.__health = Monster.WEAK
"""

"""
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return f"({self.a},{self.b})"
    
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)
    
    def __sub__(self, other):
        return Vector(self.a - other.a, self.b - other.b)
    
u = Vector(0,1)
v = Vector(1,0)
w = Vector(1,1)

a = u + v
print(a)
"""

"""
import random

class dice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 30
        self.value = 1
    
    def roll_dice(self):
        self.value = random.randint(1,6)
    
    def read_dice(self):
        return self.value
    
    def print_dice(self):
        print(self.value)
    
d = dice(100,10)
d.roll_dice()
d.print_dice()
"""

print("hi")




































