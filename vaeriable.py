'''변수(Variable) : 객체를 가르키고 있는것. 참조변수라고 한다.
aa = 100
bb = 100

is : 파이썬의 내장함수로, 2개의 변수가 서로 같은 변수를 가지고 있는지 파악하는 기능.
aa is bb
'''

aa = 100
bb = 100
cc = 100

print(aa is bb)

#변수 삭제하기
del(aa)

#변수 선언 및 초기화
cc = dd = 100 #여러개의 변수에 동일값을 대입하기 위한 방법
cc,dd = '국제시장','명량'

print(cc)
print(dd)
(cc,dd) = ('aa','bb')
print(cc)
print(dd)


#혼동하기 쉬운 예
aa = ['a','b','c']
bb = aa
aa[2] = 'd'
print(aa)
print(bb)

#데이터의 복사
aa = ['a','b','c']
bb = aa[:] #aa의 List를 처음부터 끝까지 슬라이싱
aa[2]='d'
print(aa)
print(bb)

'''식별자 만들기
    - 식별자의 첫문장은 알파뱃 문자,밑줄(_) 이 와야한다.
    - 첫문자 이외에는 밑줄(_), 숫자가 들어갈수 있다.
    - 식별자는 대/소문자를 구분한다.
      ex) myname != myName
    - 올바른 식별자 : i, aa, name_1_2
    - 잘못된 식별자 : 2name, a a b b, my-name, ?abc
'''
