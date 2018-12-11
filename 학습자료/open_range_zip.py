# open(filename,[mode])는 '파일이름'과 '읽기방법'을 입력받아 객체를 리턴하는 함수.
# w = 쓰기 모드로 파일 open
# r = 읽기 모드로 파일 open
# a = 추가 모드로 파일 open

fread = open("read_mode.txt", 'r')
fread2 = open("readmode.txt")  #모드부분이 생략되면 기본값 r을 가짐
fappend = open("append_mode.txt", 'a')


#range
a = list(range(5)) #숫자를 지정해주지 않으면, range함수는 0부터 시작
b = list(range(5,10))  #2개의 숫자는 시작과 끝숫자를 나타냄 즉 5~9
c = list(range(0,-10,-1)) #0부터 -9까지, 숫자 사이의 거리는 -1


#sort,sorted
#sort는 객체 자체를 정렬만 할 뿐, 정렬된 결과를 Return 하지 않는다.
#sorted는 객체 정렬뿐만 아니라, 결과도 Return한다.

d = [3,1,2]
result = d.sort()
print(result)   # 리턴값이 없기 때문에 None이 출력됨. 그러나 객체 d를 확인하면 [1,2,3]으로 정렬되어있음


#zip : 동일한 갯수로 이루어진 자료형을 묶어주는 역할을 하는 함수.
e = list(zip([1,2,3],[4,5,6]))
f = list(zip([1,2,3],[4,5,6],(7,8,9)))