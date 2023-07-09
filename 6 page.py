"""
temps = [28,31,33,35,27,26,25]

for i in range(len(temps)):
    print(temps[i], end=" ")

print("")

for i in temps:
    print(i, end=" ")
"""

"""
questions =['name', 'quest', 'color']    
answers = ['Kim', '파이썬', 'blue']

for q,a in zip(questions, answers): #2 개의 리스트를 묶기
    print(f"What is your {q}? it is {a}")
"""

"""
heroes = ["iron man" ,"torr", "hurk"]
n = heroes.index("hurk")
print(n)

if "hurk" in heroes:
    print(heroes.index("hurk"))
"""

"""
nums = ['hurk','dldl','xxx','yyy','zzz','kkk']
nums.remove('xxx')
print(nums)
nums.pop(1)
print(nums)
"""

"""
values = [1,3,3,9,5,11,7,13,8,10]
print(min(values))
print(max(values))
values.sort()
print(values)
values.sort(reverse=True)
print(values)
"""

"""
nums = [10,3,7,1,9,4,2,8,5,6]
ascending_nums = sorted(nums)
print(ascending_nums)
"""

"""
scores = []
n = 0
for i in range(5):
    x = int(input("성적을 입력하시오: "))
    scores.append(x)

average = sum(scores)/5
maxnum = max(scores)
minnum = min(scores)
for i in scores:
    if i >= 80:
        n+=1
print("성적 평균= ",average)
print("최대 점수= ",maxnum)
print("최소 점수= ",minnum)
print("80점 이상= ",n)
"""

"""
nums = [-7,2,3,8,6,6,75,38,3,2]
nums.sort()
print(nums[-2])
"""

"""
scores = [10.0,9.0,8.3,7.1,3.0,9.0]
print("제거전 ",scores)
scores.remove(max(scores))
scores.remove(min(scores))
print("제거후 ",scores)
"""

"""
fruits = []
for i in range(3):
    x = input("과일을 입력하시오: ")
    fruits.append(x)

for i in range(3):
    print(fruits.pop())
"""

"""
def menu():
    print("-----------------")
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")
    sel = int(input("메뉴를 선택하시오: "))
    return sel

flist = []

while True:
    user = menu()
    
    if user == 1:
        print(flist)
    
    elif user == 2:
        x = input("이름을 입력하시오: ")
        flist.append(x)
    
    elif user == 3:
        x = input("이름을 입력하시오: ")
        if x in flist:
            flist.remove(x)
        else:
            print("잘못된 이름입니다.")
    
    elif user == 4:
        x = input("삭제할 이름을 입력하시오: ")
        if x in flist:
            y = input("바꿀 이름을 입력하시오: ")
            n = flist.index(x)
            flist[n] = y
        else:
            print("잘못된 이름입니다.")
    
    elif user == 9:
        break
    else:
        continue
"""

"""
heroes1 = ["아이언맨", "토르"]
heroes2 = ["헐크", "스칼렛 위치"]
avengers = heroes1 + heroes2
print(avengers)
"""

"""
list1 = [1,2,3]
list2 = [1,2,3]
print(list1 == list2)
list1 = [3,4,5]
print(list1>list2) #첫 요소 비교 -> 2번째 요소 비교
"""

"""
temps = [28, 31, 33, 35, 27, 26, 25]
values = temps #같은 주소를 공유 얕은 복사임
print(temps)
values[3] = 39 
print(temps)
"""

"""
temps = [28, 31, 33, 35, 27, 26, 25]
values = list(temps) #깊은 복사에용
print(temps)
values[3] = 39 
print(temps)
"""

"""
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

sublist = numbers[2:7] #뒤는 안들어감
print(sublist)
print(numbers[:3])
print(numbers[3:])
print(numbers[:])
new_numbers = numbers[:] #깊은 복사
"""

"""
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[2:7:2])
print(numbers[::-1]) #step = -1
"""

"""
lst = [1,2,3,4,5,6,7,8]
lst[::2] = [99,99,99,99]
print(lst)
lst[:] = []
print(lst)
"""

"""
numbers = list(range(0,10)) #0부터 9까지 저장하는 리스트
print(numbers)
del numbers[-1] #pop, remove, del 다 되네 그냥 ㅋㅋ
print(numbers)
"""

"""
numbers= list(range(1,11))
print(numbers[::-2])
del numbers[1:] #슬라이싱해서 없애려면 del만 이용해야하는 것 같기도 함 or numbers[1:] =[] 이게 나을듯
print(numbers)
"""

"""
def func1(x):
    x= 42 #새로운 객체 생성
    print("x=",x,"id=",id(x))

y= 10 #불변 객체임
func1(y)
print("y=",y,"id=",id(y))

def func2(list): 
    list[0] = 99

values = [0,1,1,2,3,5,8] #리스트는 가변 객체라서 함수에 넣으면 바뀜
func2(values)
print(values)
"""

"""
list1 = [200,250,300,280,500]

def modify(list):
    for i in range(len(list)):
        list[i] = (130/100)*list[i]

modify(list1)
print(list1)
"""

"""
squares = [x*x for x in range(10)]
print(squares)

squares = [x*x for x in range(10) if x % 2 == 0]
print(squares)
"""

"""
prices = [135, -545, 922, 356, -992, 217]
mprices = [i if i > 0 else 0 for i in prices]
print(mprices)

words = ["All", "good", "thing", "must", "come", "to", "an", "end."]
letters = [w[0] for w in words]
print(letters)

numbers = [x+y for x in ['a','b','c'] for y in ['x','y','z']]
print(numbers)
"""

"""
numbers = list(range(0,100))
new_numbers = [i for i in numbers if i % 2 == 0 and i % 3 == 0 ]
print(new_numbers)
"""

"""
flist = [10,20,30,40,50]
nlist = [sum(flist[:i+1]) for i in range(len(flist))]
print(nlist)
"""

"""
tlist = [(x,y,z) for x in range(1,31) for y in range(1,31) for z in range(1,31) if x**2 + y**2 == z**2 and x<y<z]
print(tlist)
"""

"""
s = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]
print(s[0][1])
"""

"""
rows = 3
cols = 5
s = []
for row in range(rows):
    s +=[[0]*cols] #2차원
print("s=",s)

s= []
for row in range(rows):
    s += [0]*cols #1차원
print("s=",s)
"""

"""
s = [ 
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]
rows = len(s)
cols = len(s[0])

for r in range(rows):
    for c in range(cols):
        print(s[r][c], end=",")
    print()
"""

"""
table=[]

for row in range(10):
    table += [[0]*10]

def init(table):
    for i in range(10):
        for j in range(10):
            if (i+j) % 2 == 0:
                table[i][j] = 1

init(table)

for r in range(10):
    for c in range(10):
        print(table[r][c], end= " ")
    print()
"""

"""
matrix = [[i for i in range(5)] for j in range(6)]
print(matrix)

matrix = [[0,0,0], [1,1,1], [2,2,2]]
result = [num for row in matrix for num in row]
print(result)
"""

"""
table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def print_matrix(table):
    for r in range(3):
        for c in range(3):
            print(table[r][c], end = " ")
        print()

def tmatrix(table):
    Ttable = []
    for i in range(3):
        Ttable += [[0]*3]
    for r in range(3):
        for c in range(3):
            Ttable[r][c] = table[c][r]
    return Ttable

print_matrix(table)
print()
print_matrix(tmatrix(table))
"""











