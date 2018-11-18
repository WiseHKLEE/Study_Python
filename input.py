import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


'''
* input 함수
'''

print('안녕하세요!!''반갑습니다.')
print('안녕하세요!!'+'반갑습니다.')

print('안녕하세요!!','반갑습니다.')  #문자열에서 콤마(,)는 띄어쓰기의 역할

for i in range(5):     #range 인수가 한개인 경우 0이 생략됨
    print(i,end=' ')   #end파라미터는 마지막 문자를 지정하는 인수이다.
