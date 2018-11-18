import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#import를 이용한 Module 입력방법(Module : 함수와 변수들을 모아놓은 것 (ex - sys,...))
'''
import sys  #파이썬에서 제공하는 Module (DOS 명령중에 type이라는 기능을 구현하기 위해서 필요한 sys Module를 가져온다.)
'''

args = sys.argv[1:]
for i in args:
    print(i)
    
