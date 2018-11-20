'''
 제어문 (조건문, 반복문) : 프로그램의 흐름을 효율적으로 이용하기 위한 것
    - 조건문 : if문
    - 반복문 : while, for문

** if문 기본 구조 **

if <조건문>:
    <실행할 명령문>
    <실행할 명령문>
else :
    <실행할 명령문>
    <실행할 명령문>

 - if 조건문 다음에는 반드시 ':'이 와야 한다.
'''

number = 1; #일반적으로 파이썬은 문장 끝 세미콜로';' 생략
print(number);

if number:
    print('0이 아니다.')
else:
    print('0이다.')

'''
**비교 연산자

< > == != >= <=

** 논리 연산자 (and, or, not)

x and y : x와 y 모두 참
x or y : x, y 둘중에 하나만 참일때 참
not x : x가 참이면 거짓

** in 연산자
x in 리스트, x not in 리스트, x in 튜플, x not in 튜플
'''

print('a' in ['a','b','c'])

print('a' not in ['a','b','c'])

'a' in ('a','b','c')

print ('a' in 'abcd')


# 이중 if 문
aa = ['a','b']

flag = 1
if 'c' in aa:
    print('a를 가지고 있습니다.')
else :
    if flag:
        print('a를 가지고 있습니다.')
    else:
        print('a를 가지고 있지 않습니다.')

#elif (=else if)

if 'c' in aa:
    print('c를 가지고 있습니다.')
elif 'a' in aa:
    print('c는 없고 a는 가지고 있습니다.')
else:
    print('a와 c가 aa에 없습니다.')

'''다중 if문의 구조
if <조건문>:
    <실행할 명령문1>
    <실행할 명령문2>
    ...
elif <조건문>:
    <실행할 명령문1>
    <실행할 명령문2>
    ...
elif <조건문>:
    <실행할 명령문1>
    <실행할 명령문2>
    ...
...
else <조건문>:
    <실행할 명령문1>
    <실행할 명령문2>

** pass
'''

aa = ['a','b','c']
dd = 'd'
if dd in aa:
    pass
else:
    print(dd+'c는 없습니다')

pp = ['a','b','c']

#if를 단일 문으로 처리하는 예
if dd in pp: pass
else: print('없습니다.')
