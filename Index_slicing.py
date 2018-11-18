import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

''' 리스트 (list)
 : 다른 언어의 배열과 같은 형태를 의미함

ex)
aa = [10,20,30]
movies = ['트랜스포머', '국제시장', '명량']
bb = [10,20,'명량', '국제시장']
cc = [10,20,["명량", "국제시장"]]
dd = [] (빈 list)
** 리스트 내에는 어떠한 자요형도 포함시킬 수 있다.

리스트의 인덱싱과 슬라이싱
'''

aa = [10,20,30]

print(aa[0])
print(aa)
print(aa[1]+aa[2])
print(aa[-1]) #인덱스값이 음수인경우 뒤에서부터 가리킨다.
bb = [10,20,30,['ab','cd','ef']]

print(bb[0])
print(bb[-1])
print(bb[3])
print(bb[3][1])

cc = [10,20,['aa','bb','cc',['국제시장','명량']]]
print(cc[2][3][0]) #삼중리스트구조에서 인덱싱

#리스트의 슬라이싱
ab = [1,10,100,1000,10000]
print(ab[:3])

ab = "110100100010000"
print(ab[:3])

bc = [1,10,100,['aa','bb','cc'],1000,10000]
print(bc[2:5])
print(bc[3][1:])

#리스트 연산(+, *:반복)
aa = [10,20,30]
bb = [100,200,300]
print(aa+bb)
print(aa*2)
print(aa[0]+bb[1])

#리스트 값 변경하기
print(aa[1])
aa[1]=100 #문자열,튜플 형의 요소의 값은 변경할 수가 없지만, 리스트는 변경 가능.
print(aa)

print(aa[2:])
aa[2:] = ['국제시장', '명량']
print(aa)

print(aa[1:3])
aa[1:3] = ['백','천','만']
print(aa)

aa[4] = ['십만', '백만', '천만']

print(aa)

# 9/1

aa[1:4] = []   # list 요소 삭제 : index 1 ~ 4까지 삭제
print(aa)

del aa[0] # del함수를 이용한 삭제 방법 del(파이썬 내장함수)
print(aa)


''' 튜플 (tuple) : list와 비슷
    - list와 tuple의 차이점
    1) list는 [], tuple은()를 사용한다
    2) list는 요소의 변경(수정,삭제,생성)이 가능하지만, Tuple은 요소값 변경 불가.

    ex)
    tu = () -> 빈값
    tu2 = (1,)
    tu3 = (10,20,30,40)
    tu4 = 10,20,30
    tu5 = ("국제시장", "명량", ("ab","cd"))

Tuple의 인덱싱, 슬라이싱, 연상
'''

tu = ('a','b','c',10,1000)
print(tu[0])

print(tu[1:4])
print(tu[2:])

tu2 = ('d','e','f')
print(tu+tu2)
print(tu*3)

#del tu2[2]  #Tuple은 문자열처럼 요소를 변경하는것을 허용하지 않는다.
