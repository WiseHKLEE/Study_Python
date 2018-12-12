from time import time, localtime, asctime, ctime, strftime, sleep #from time import * 로 해도 무방하다.

a = time() #time은 UTC(Universal Time Coordinated : 협정 세계 표준 시)를 이용하여 현재 시간을 실수형태로 리턴하는 함수.
print(a)

b = localtime(a) #localtime은 time()에 의해서 반환된 실수값을 이용해서 연도, 월, ... , 분, 초의 형태로 변경
print(b)

c = asctime(b) #asctime은 localtime에 의해서 반환된 tuple형태의 값을 인수로 받아서 보기쉬운 형태로 리턴하는 함수
print(c)

d = ctime()  #asctime(localtime(time())) == ctime(). 다만 현재시간만 리턴.
print(d)

e = strftime('%x', b)
print(e)

f = strftime('%c', b)
print(f)

for i in range(10): #sleep은 주로 루프와 자동화에 많이 사용된다. 이 함수를 사용하면 일정한 시간 간격을 두고 코드를 실행할 수 있다.
    print(i)        #해당 Case는 1초 간격으로 0~9까지 출력
    sleep(1)