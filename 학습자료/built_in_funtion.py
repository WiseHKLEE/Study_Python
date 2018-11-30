#내장함수
abs1 = abs(3)  # 절대값표시
abs2 = abs(-3)
abs3 = abs(-1.2)
print(abs1)
print(abs2)
print(abs3)

all1 = all([1,2,3])  #all은 반복 가능한 자료형 x를 입력 인수로 받으며, x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴 (and와 비슷)
print(all1)
all2 = all([1,2,3,0])  #0이 거짓이므로 False를 리턴한다.
print(all2)

any1 = any([1,2,3,0]) #any는 x중 하나라도 참일 경우 True, 전부 거짓이면 False를 리턴한다. (or와 비슷)
print(any1)
any2 = any([0,""]) #둘다 거짓이므로 False를 리턴한다.
print(any2)

chr1 = chr(97) #chr는 아스키(ASCII)코드값을 입력으로 받아 그 코드에 해당하는 문자를 출력하는 함수.
print(chr1)
chr2 = chr(48)
print(chr2)

dir1 = dir([1,2,3])  #dir은 객체가 자체적으로 가지고 있는 변수나 함수를 출력한다.
print(dir1)    #list가 가지고 있는 함수
dir2 = dir({'1':'a'})
print(dir2)    #dictionary가 가지고 있는 함수

div1 = divmod(7,3) #divmod는 2개의 숫자를 입력으로 받으며, a를 b로 나눈몫과 나머지를 튜플형으로 출력
print(div1)
div2 = divmod(1.3, 0.2)
print(div2)

for i, name in enumerate(['body', 'foo', 'bar']): #enumerate는 순서가 있는 자료형(list,tuple,문자열)을 입력으로 받아 index값을 포함하는 enumerate객체로 리턴한다.
    print(i,name)

eval1 = eval('1'+'2')  #eval은 실행가능한 문자열을 입력으로 받아 문자열을 싱핼한 결과값을 리턴. 함수 or 클래스를 동적으로 실행하고 싶은 경우에 사용
print(eval1)
eval2 = eval('1+2')
print(eval2)
eval3 = eval('"hi"+"a"')
print(eval3)
eval4 = eval('divmod(4,3)')
print(eval4)

