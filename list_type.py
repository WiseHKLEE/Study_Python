import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

aa = "ABCD"
print(aa[1])

#aa[1]='F' #문자열, 튜플 자료형은 그 요소값을 변경할 수 없다.
#print(aa[1])

aa[:1]
print(aa[:1])
aa[2:]
print(aa[2:])

aa = aa[:1]+'F'+aa[2:]
print(aa)

'''문자열 formmatting : 문자열 내에 어떤 특정 값을 변화시키는 방법
  ex) 현재 날짜는 8월 25일입니다.
     ...
     ...
      현재 날짜는 8월 26일입니다.'''

#숫자 대입
print('제 나이는 %d살입니다.' %20)
print('제 나이는 %d살입니다.' %21)

#문자 대입
print('제 이름은 %s입니다.' %"홍길동")
print('제 이름은 %s입니다.' %"고길동")

#숫자형 변수 대입
age = 22
print("제 나이는 %d살입니다." %age)

#여러개의 값을 대입
age = 28
name = "소솔"
print("저의 이름은 %s입니다. 나이는 %d입니다." %(name, age))

''' 포맷 코드
%% = 리터럴 %
%s = 문자열(String)
%d = 정수(Integer)
%f = 실수형(float)
%c = 문자(character)
%o = 8진수
%x = 16진수
'''

print('완치될 확률을 %d%%입니다.' %70)

''' 포맷코드의 활용 예
1. 소수점 표현하기'''

print("%.2f" %0.5353)

# 정렬과 공백처리
print('%10s' %"hello")
print('%-10s' %"hello")
print("%-7sPython!!" %"hello")
