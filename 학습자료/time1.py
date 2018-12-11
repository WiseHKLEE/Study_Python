from time import time  #time은 UTC(Universal Time Coordinated : 협정 세계 표준 시)를 이용하여 현재 시간을 실수형태로 리턴하는 함수.
a = time()
print(a)

b = time.localtime(time())
print(b)