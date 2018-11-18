'''
 * 파일 입출력
 1) 파일 생성
  - 파일 객체 = open(파일이름, 파일 열기모드)
  ※ 파일 열기 모드?
  - 읽기 모드 (r) : 파일을 읽기위한 용도로 사용할 때
  - 쓰기 모드 (w) : 파일에 내용 작성할 때 (쓰기모드로 열 때 원래있던 내용은 삭제되고 열린다.)
  - 추가 모드 (a) : 파일에 새로운 내용을 추가할 때

'''

fp = open('test_new.txt', 'w')


fp.close()  #파이썬에서는 Close는 생략해도 무방하나, 해당 명령어를 넣어주는것이 올바른 방법.


#파일에 내용을 출력하기
fp = open('test_new.txt', 'w')
for i in range(1,5):
    content = "%d 번째 라인.....\n" %i
    fp.write(content)    #txt파일에 작성

fp.close()

for i in range(1,10):
    content = "%d 번째 줄....\n" %i
    print(content)    #모니터에 출력


'''
2) 파일 읽어오는 방법
 .readline() :
'''

fp = open('test_new.txt','r')
data = fp.readline() #읽어온 Data를 Rerutn한다. Return 하기 위해서는 받아야할 변수가 필요함
print(data)
fp.close()

fp = open('test_new.txt','r')

while True:
    data = fp.readline() #더이상 파일에서 읽어올 line이 없는 경우에는 None 리턴
    if not data: break
    print(data)

'''
while 1:
    userData = input() #사용자가 입력한 Data
    if not userData: break
    print(userData)
'''

'''
 .readlines() 를 이용하여 File 읽어오기
'''

fp = open('test_new.txt','r')
datas = fp.readlines() #readlines()는 Return값이 List이다.
                       #이 함수는 모든 라인을 읽어서 List에 Return 한다.

for i in datas:
    print(i) #i는 ['1 번째 라인....\n', '2 번째 라인....\n', '3 번째 라인....\n', '4 번째 라인....\n']

fp.close()


'''
.read()함수를 이용한 파일 읽기
'''

fp = open('test_new.txt','r')
data = fp.read() #read()함수는 파일 내용 전체를 문자열로 Return 한다. 즉, List가 아닌 문자열.
print('===========')
print(data)

fp.close()


#a 모드를 이용해서 파일에 내용을 추가하기

fp = open('test_new.txt','a')

for i in range(5,8):
    data = '%d 번째 라인.....\n' %i
    fp.write(data)

fp.close()

#with문을 이용해서 File 객체 다루기 : with문을 이용하면 file을 닫을 필요가 없다. 자동으로 닫아줌
fp = open('test_2.txt','w')
fp.write('파일 입출력 Test 2번째')
fp.close()

with open('test_2.txt','w') as fp:
    fp.write('with문을 이용한 File 입출력 Test')
