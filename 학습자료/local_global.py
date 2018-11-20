'''
* 변수의 Scope
 - 사용자가 정의한 함수 안에서 선언된 변수는 그 함수 밖에서는
   사용불가. 즉, 그 변수의 범위는 함수 안에서만 유효하다.
   이렇게 함수의 지역(local)을 변수의 Scope라고 한다.
   함수 내에서 선언된 변수를 지역 or local 변수라고 한다.
'''

'''
* 지역 변수(local)
'''

a = 20 #전역변수(global 별수) 여기서 선언된 변수 a는 프로그램이 종료 될때까지 유효하다.

def func(a): #()안에 a라는 매개변수(인수)는 로컬변수, func함수에서 선언된 지역변수
    print('a는',a)
    a = 10
    print('로컬변수 a는', a)

func(a)
print(a)

def func1(b):
    b=b+1
    print(b)

func1(30)

# print(b) : 여기서 b는 존재하지 않는 변수


'''
* 전역(global)변수
'''

aa = 10
def aa_func(aa):
    aa += 1
    return aa

aa = aa_func(aa) #return문을 사용해서 함수 밖에서 선언된 변수의 값을 변경시키는 예
print(aa)

bb = 100

def bb_func():
    global bb #global은 함수밖의 변수를 직접 사용하겠다라는 의미
    bb = bb+1

bb_func()
print(bb)

#될 수 있으면 global 문을 사용하지 않는것이 바람직하다.
# global문을 사용하는것 보다는 return문을 사용하는것이 좋다.
