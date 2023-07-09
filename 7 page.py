"""
fruits = () #공백 튜플 생성
fruits = ("apple", "banana", "grape") # 초기값 가진 튜플 생성
result = fruits[1] #인덱스 사용해서 접근
fruits = "apple", "banana", "grape"
fruits = ("apple",) #끝에 쉼표가 있어야 함, 쉼표 없으면 수식이 된다.
"""

"""
fruits = ("apple", "banana", "grape")
fruits[1] = "pear" #오류 발생 튜플은 값 변경 불가능
"""

"""
fruits = ("apple", "banana", "grape")
fruits += ("pear", "kiwi") #붙이는 건 가능
print(fruits) 

numbers = [10, 20, 30]
numbers += [40, 50]
print(numbers)
"""

"""
fruits = ("apple", "banana", "grape")
for index, value in enumerate(fruits):
    print(index, value)
"""

"""
numbers = {1,2,3} #세트
values = set() #공백 세트 생성
letters = set("abc")
print(letters)
"""

"""
fruits = {"apple", "banana", "grape"}
for x in fruits:
    print(x, end=" ")

fruits.add("kiwi") #세트에만 있음
fruits.remove("banana") #fruits.discard("banana") 도 가능
print(fruits)
"""

"""
A = {"apple", "banana", "grape"}
B = {"apple", "banana", "grape", "kiwi"}
if A <= B: # ==, != 도 가능 
    print("A는 B의 부분 집합입니다.")
"""

"""
A = {"apple", "banana", "grape"}
B = {"apple", "banana", "kiwi"}

C = A|B #합집합
print(C)

D = A & B #교집합
print(D)

E = A - B #차집합
print(E)
"""

"""
list1 = [1,2,3,4,5,1,2,4]
print(len(set(list1)))
"""

"""
A = input("첫 번째 문자열: ")
B = input("두 번째 문자열: ")
C = set(A) & set(B)
C.remove(" ")
for i in C:
    print(i, end=" ")
"""

"""
A = input("입력 텍스트: ")
B = A.split(" ")
C= set(B)
print("사용된 단어의 개수= ", len(C))
print(C)
"""

"""
capitals = {}
capitals["Korea"] = "Seoul"
capitals["USA"] = "Washington"
capitals["UK"] = "London"
print(capitals)

if "UK" in capitals:
    capitals.pop("UK")
print(capitals)
"""

"""
capitals = {"Korea":"Seoul", "USA":"Washington", "UK":"London"}

for key in capitals:
    print(key,":",capitals[key])

for key, value in capitals.items():
    print(key,":",value)
"""

"""
values=[1,2,3,4,5,6]
dic = {x: x**2 for x in values if x%2==0}
print(dic)

dic = {i:str(i) for i in [1,2,3,4,5]}
print(dic)

fruits = ["apple", "orange", "banana"]
dic = {f:len(f) for f in fruits}
print(dic)
"""

"""
words = {"one":"하나","two":"둘"}
x = input("단어를 입력하시오:")

if x in words:
    print(words[x])
"""

"""
def display_menu():
    print("1.연락처 추가")
    print("2.연락처 삭제")
    print("3.연락처 검색")
    print("4.연락처 출력")
    print("5.종료")
    sel = int(input("메뉴 항목을 선택하시오: "))
    return sel

flist = {}

while True:
    user = display_menu()
    if user == 1:
        x = input("이름: ")
        y = input("전화번호: ")
        flist[x] = y

    elif user == 2:
        x = input("삭제할 이름: ")
        if x in flist:
            flist.pop(x)
        else:
            print("잘못된 이름입니다.")
    
    elif user == 3:
        x = input("찾을 이름을 입력하세요: ")
        if x in flist:
            print("이름: ",x, "전화번호: ", flist[x])
        else:
            print("잘못된 이름입니다.")
    
    elif user == 4:
        for key, value in flist.items():
            print("이름: ",key, "전화번호: ", value)
    
    elif user == 5:
        break

    else:
        continue
"""

"""
score_dic = {
    "kim":[99,83,95],
    "lee":[68,45,78],
    "Choi":[25,56,69]
}

def get_avg(dic):
    for key in dic:
        sum1 = sum(dic[key])/3
        print(key,"의 평균성적= ",sum1)

get_avg(score_dic)
"""

"""
X = input("문장을 입력하시오: ")
Y = X.split(" ")

words_dic = {}

for words in Y:
    if words not in words_dic:
        words_dic[words] = 1
    else:
        words_dic[words] += 1

for key, value in words_dic.items():
    print(key,"의 등장횟수= ",value)
"""

"""
from collections import Counter
X = input("문장을 입력하시오: ")

a = Counter(X.split()) #Counter가 딕셔너리 형태로 바꿔주는듯
print(a)
"""
"""
print(chr(97)) #정수를 문자로
print(ord("a")) #문자를 아스키 코드로 바꿈
"""

"""
reg = "980326"
print(reg[0:2]+"년")
print(reg[2:4]+"월")
print(reg[4:6]+"일")
"""

"""
word = "abcdef"
word[0] = "A" #문자열은 불변 객체! 리스트는 가변객체 따라서 오류 발생
print(word)
"""

"""
a = input("문자열을 입력하시오:")
b = input("문자열을 입력하시오:")

if (a < b): #사전상으로
    print(a+"가 앞에 있음")
else:
    print(b+"가 앞에 있음")
"""

"""
X = input("문자열을 입력하시오: ")
Y = X[::-1]

if X == Y:
    print("회문입니다.")
else:
    print("아닙니다.")
"""

"""
s = "i am a student"

if len(s) > 0: #맨 앞 글자만 대문자로
    print(s[0].upper()+ s[1:])
else:
    print("wrong")

s = "Breakfast At Tiffany"
print(s.lower()) #전부 소문자
print(s.upper()) #전부 대문자
"""

"""
s = input("파이썬 소스 파일 이름을 입력하시오: ")
if s.endswith(".py"): # 이 문자로 끝나는지 확인하는 함수
    print("올바른 파일 이름입니다.")
else:
    print("올바른 파일 이름이 아닙니다.")
"""

"""
s = "www.naver.com"

k = s.replace("com","co.kr") #대체해줭
print(k)

print(k.find("kr")) #.kr의 시작위치 알려줘

s= "let it be, let it be, let it be"
print(s.rfind("let")) #오른쪽부터 시작하는 let을 찾아줘

print(k.count("."))
"""

"""
print("ABCabc".isalpha())
print("123.4".isdigit()) #모두 숫자로만 이루어져야하는데 "."은 숫자가 아님
print("abc".islower())
"""

"""
s = " Hello World!   "
print(s.strip())

s = "#############this is example ##########"
print(s.strip("#"))
print(s.lstrip("#"))
print(s.rstrip("#"))
"""

"""
s = "Welcome to Python"
print(s.split()) #띄어쓰기로 나누기
print(list(s)) #한 글자씩 쪼개기
"""

"""
print(",".join(["apple","grape","banana"])) # 한 문장으로 모으기 ","로 묶으면서
print("-".join("010.1234.5678".split(".")))
"""

"""
X = input("문자열을 입력하시오: ")
Y = X.split()

s = ""
for words in Y:
    s += words[0]
print(s)
"""

"""
X = input("이메일 주소를 입력하시오: ")
print(X)

s = X.find("@")
print("아이디:", X[:s])
print("도메인:", X[s+1:])
"""

"""
address = input("이메일 주소를 입력하시오: ")
(id, domain) = address.split("@")
print(address)
print("아이디:"+id)
print("도메인:"+domain)
"""





