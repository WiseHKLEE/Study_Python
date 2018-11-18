import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

'''for문

for문의 기본구조

for 변수 in 리스트(tuple,문자열):
    <실행할 문장1>
    <실행할 문장2>
    ...
'''

list1 = ['a','b','c']

for i in list1:
    print(i)

score = [90,50,60,44,30] #1번부터 5번학생의 점수

number = 0


for i in score:
    number = number+1
    if i >= 60:
        print('%d번 학생의 점수는 %d점으로 합격입니다.' %(number,i))
    else:
        print('%d번 학생의 점수는 %d점으로 탈락입니다.' %(number,i))

number = 0
for i in score:
    number = number+1
    if i<60:
        continue
    print('%d번 학생 합격입니다.' %number)


aa = [('a','b'),('c','d'),('e','f')]
for (i,j) in aa:
    print(i+j)

''' for문과 range 함수

range 함수는 2개의 숫자를 이용하는 함수이다.
숫자가 2개입력된 경우, 1씩 증가하는 숫자의 list를 반환한다.
(*두번째 숫자의 의미는 해당숫자 이하가 아닌 미만을 의미한다.)
숫자가 3개입력된 경우, 마지막숫자는 증가치를 의미한다.

ex)
range(1,5) ---> list [1,2,3,4] 반환
range(1,5,2) ---> list[1,3]

'''

for i in range(1,5):
    print(i)
else:  #반복문에서 else절은 loof를 다 돌고난 뒤에 수행한다. break문을 사용했을 경우네는 수행되지 않는다.
    print('반복문 종료')

''' c언어에서 for문과 python의 for문은 근본적으로 다르다.
    Python의 for문은 C# foreach와 비슷하고, java의 for(int i : IntArray)와 비슷하다.
    c언어에서 for(int i = 0; i<5; i++)

[구구단 표현]
'''

for i in range(2,10):
    for j in range(0,10):
        k = i*j
        print('%d*%d=%d' %(i,j,k), end=' ')
    print(' ')

''' list 내에 for문을 이용하여 진행 '''

aa = [1,2,3,4,5,6,7,8,9]

res_2 = []

for i in aa:
    res_2.append(i*2)
print(res_2)

res_2 = [i*2 for i in aa]
print(res_2)

#5단의 결과값중 짝수만 list에 추가할 경우
res_5 = [i*5 for i in aa if i%2 == 0]
print(res_5)


'''list 내포(List comprehension)의 일반적인 구조
1. [표현식 for 항목(i) in 반복가능한 객체(aa) if 조건]
    위에서 if 조건은 생략 가능
2. [표현식 for 항목1 in 반복가능한 객체 if 조건1
          for 항목2 in 반복가능한 객체 if 조건2
          ....
          for 항목n in 반복가능한 객체 if 조건n]
'''

#구구단의 결과를 저장하는 list 구현
res = [i*j for i in range(2,10)
           for j in range(1,10)]
print(res)
