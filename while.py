import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

''' while문
while문의 구조

while <조건문>:
    <실행할 명령문1>
    <실행할 명령문2>
    <실행할 명령문3>
    ...
'''

aa = 0
while aa < 10:
    aa = aa+1
    print ('aa값은 %d입니다.' %aa)
    if aa == 10:
        print('종료합니다.')

''' 무한루프 예

while 1:
    <실행할 명령문>
    ...
'''

'''보조제어문(break, continue)
    countinue : 다시 조건문으로 돌아간다.
    break : 조건문을 중단(탈출)한다.'''

m = 100
n = 10
while m:
    print('현재 %d 입니다.' %n)
    n = n-1

    if not n:
        print('n의 값이 0입니다.')
        break #제어문 탈출

# 1~10까지 정수중 홀수 출력하는 코드
i = 0
while i < 10:
    i = i+1
    if i%2 == 0: continue  #다시 조건문으로 넘어간다.
    print(i)
