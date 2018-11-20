import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


'''함수(function) : 재사용 가능한 프로그램, 명령 덩어리
    우리가 접했던 함수 range(1,5) 는 이미 만들어져 있는(내장되어 있는)
    앞에서 우리는 range()함수를 호출해서 사용했다.

    함수는 프로그램을 작성할 때 필요한 중요한 기능이다.

    함수에는 내장함수, 사용자 정의함수로 구분

    함수 사용 이유? 사용성을 위해서.

    [문자열 함수]
    문자열 formmatting 함수중 format()
'''
# {n}은 자리표시를 의미한다. n은 숫자
print("you've {0} a friend".format("got"))
str = "{2} {0} {1}".format("a",10,200)
print(str)

number = 100
day = "sunday"

print('오늘은 우리가 사귄지 {0}일째 되는 날! 요일은 {1}!'.format(number, day))

#index와 이름을 혼용해서 사용하기
print('오늘은 우리가 사귄지 {0}일째 되는 날! 요일은 {day}'.format(300,day='sunday'))

#좌측 정렬
name='소솔'
print('{0:<10}'.format(name))

#우측 정렬
print('{0:>10}'.format(name))

#가운데 정렬
print('{0:^10}'.format(name))

print('{0:-^20}'.format(name))

#소문자를 대문자로 바꾸는 함수
aa = 'hello'
aa1 = aa.upper()

print(aa)
print(aa1)

#대문자를 소문자로 바꾸는 함수
aa2=aa1.lower()
print(aa2)

#문자 갯수를 리턴하는 함수

aa = "abcdefd"
cnt = aa.count('d')
print(cnt)

#문자열의 길이 구하는 함수
cnt = len(aa)
print(cnt)

#문자의 위치 찾기 : 문자열에서 찾고자 하는 문자의 첫번째 위치 리턴
bb = 'cafdefgfff'
loc = bb.find('f') #찾고자 하는 문자가 없을 경우에는 -1을 반환한다.
print(loc)

loc = bb.index('f') #찾고자 하는 문자가 없을 경우에는 에러가 발생한다.
print(loc)

#공백지우기 함수(lstrip, strip, rstrip)
aa = '   good   '
print(aa.lstrip() + 'morning')
print(aa.strip() + 'morning')
print(aa.rstrip() + 'morning')

#문자열 대체 함수(replace)
aa = 'good morning Jane!!'
bb = aa.replace('morning', 'night') #바꿀 대상, 바뀌는 문자
print(bb)

#문자열 나누기 함수(split)
str = 'good morning sol!!'
str_split = str.split() #split괄호안에 값이 없으면 공백 기준으로 나눔
print(str_split)

str = '소솔/28/경기도 안양시/111-2345-6789'
print(str.split('/')) #/를 구분자로해서 문자열을 나눔. 그 결과는 list에 저장
