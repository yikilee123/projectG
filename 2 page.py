"""
import turtle
t=turtle.Turtle()
t.shape("turtle")

radius = 50
t.circle(radius)
t.fd(30)
t.circle(30)
t.fd(30)
t.circle(50)

turtle.mainloop()
turtle.bye()
"""

"""
light=300000

distance=40*10**12

stime=distance/light
htime=stime/3600
dtime=htime/24
ytime=dtime/365
print(ytime,"광년")
"""

"""
x=y=z=0
x,y,z = 10,20,30
x,y = y,x
print(x,y)
"""

"""
x=0.06
y=24*(1+x)**382
print(y)
"""

"""
price = 12345
tax = price * 0.075
tax = round(tax,2) # 2째 자리까지 반올림
print(tax)
"""

"""
#message = "철수가 "안녕"이라고 말했습니다." #syntax error

message = "철수가 '안녕'이라고 말했습니다."

print(message)
"""

"""
print(100+200)
print("100"+"200")
"""

"""
print("말 한 마디로\n천 냥의 빚을 갚는다.")
"""

"""
x="100"
print(int(x))
"""
"""
name = input("이름을 입력하시오:")
print(name,"씨, 안녕하세요? \n파이썬에 오신 것을 환영합니다.")
x=int(input("첫 번째 정수를 입력하시오:"))
y=int(input("두 번째 정수를 입력하시오:"))
print(x,"과",y,"의 합은",x+y,"입니다.")
"""

"""
x=3.3

area=int(input("면적:"))
py = area/x
print(py)
"""

"""
x=100
y=200
print(f"{x}와 {y}의 합={x+y}")
"""

"""
x = float(input("몸무게를 kg 단위로 입력하시오:"))
y = float(input("키를 미터 단위로 입력하시오:"))
z = x/(y**2)
print("당신의 BMI=",z)
"""

"""
x = float(input("반지름을 입력하시오:"))
print((4/3)*3.14*(x**3))
"""

"""
price = int(input("물건 값을 입력하시오:"))
x = int(input("1000원 지폐개수:"))
y = int(input("500원 동전개수:"))
z = int(input("100원 동전개수:"))
money = 1000*x+500*y+100*z
k = money - price

if k<0:
    print("can't buy")
elif k>=0:
    x1 = k//1000
    r1 = k % 1000
    y1 = r1//500
    r2 = r1 % 500
    z1 = r2//100
    r3 = r2%100
    k1 = r3//10
    r4 = r3%10
    print(x1,y1,z1,k1)
"""


















