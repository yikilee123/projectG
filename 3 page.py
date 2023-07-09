"""
price = int(input("상품의 가격:"))
if price > 20000:
    shipping_cost = 0
else:
    shipping_cost = 3000
print("배송비=", shipping_cost)
"""

"""
r = 100
flag = r>32 #조건문은 대신할 수 있음
print(flag)

expensive = pice > 20000
if expensive:
    shipping_cost = 0
else:
    shipping_cost = 3000
"""

"""
s1 = "Audrey Hepburn"
s2 = "Grace Kelly"
print(s1 < s2) #첫 글자부터 비교
"""

"""
from math import sqrt

n = sqrt(3.0)
if n*n ==3.0:
    print("같다")
else:
    print("다르다") # 무리수 전부 저장하기 어렵기 때문에 유효숫자까지 저장! 그래도 근접하긴 함 -->sqrt(3.0)이 정확히 루트 3이 아님

if abs(n*n-3)<0.0000001:
    print("같다잉")
"""

"""
x = int(input("정수를 입력하시오:"))

if x%2==0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
"""

"""
x = int(input("정가를 입력하시오:"))

if x<100:
    print("할인된 가격=",x*(9/10))
else:
    print("10층에서 사은품을 가져가세요.")
    print("할인된 가격=",x*(85/100))
"""

"""
x = int(input("온도를 입력하시오:"))

if x<0:
    print("ice")
elif 0<x<100:
    print("water")
else:
    print("gas")
"""

"""
import random

print("동전 던지기 게임 시작")
x = ["앞면","뒷면"]
y = random.choice(x)
if y =="앞면":
    print("lose")
else:
    print("win")
"""

"""
location = input("배송지(us or korea):")
price = int(input("상품의 가격:"))

if location == "korea":
    if price >= 20000:
        print("배송비=",0)
    else:
        print("배송비=",3000)
else:
    if price >= 100000:
        print("배송비=",0)
    else:
        print("배송비=",8000)
"""

"""
score = int(input("성적을 입력하시오:"))

if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")
"""

"""
def menu():
    print("===================")
    print("메뉴 1번: 치즈 버거")
    print("메뉴 2번: 치킨 버거")
    print("메뉴 3번: 불고기 버거")
    print("메뉴 4번: 나갈랭")
    print("===================")
    sel = int(input("메뉴를 고르세요:"))
    return sel

while True:
    user = menu()
    if user == 1:
        print("여기 치즈 버거")
        break
    elif user == 2:
        print("여기 치킨 버거")
        break
    elif user == 3:
        print("여기 불고기 버거")
        break
    elif user == 4:
        print("나갈랭~~~")
        break
    else:
        print("다시 골라")
"""

"""
import random

slist = ["왼쪽","오른쪽","중앙"]

x = input("어디를 막을래?")
y = random.choice(slist)

if x == y:
    print("막음")
else:
    print("못막음")
    print("답은",y)
"""

"""
slist =[]

for i in range(3):
    x = int(input("삼각형의 한 변을 입력하시오:"))
    slist.append(x)

slist.sort(reverse=True)

if slist[0] < slist[1] + slist[2]:
    print("올바른 삼각형")
else:
    print("이건 삼각형이 안돼")
"""

"""
def f(x): #이분법으로 해 찾기
    return x**2-x-1

a = 0
b = 50
m = (a+b)/2

while abs(f(m)) > 0.0001:
    if f(a)*f(b) < 0:
        b = m
    else:
        b = 2*b - a
        a = (a+b)/2
    m = (a+b)/2

print(m)
"""














