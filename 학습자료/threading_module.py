import threading
import time

def say(msg):
    while True:
        time.sleep(1)
        print(msg)

for msg in ['you','need','python']:
    t = threading.Thread(target=say, args=(msg,))  #for문에서 생성된 list의 요소 개수 만큼 Thread가 생성되고, 생성된 Thread는 say메 메서드를 수행하게 되어 1초에 한번씩 입력으로 받은 msg변수값 리턴.
    t.daemon = True    #daemon 플래그를 설정하면 주 프로그램이 종료되는 순간 해당 Thread도 함께 종료.
    t.start()

for i in range(100):
    time.sleep(0.1)
    print(i)