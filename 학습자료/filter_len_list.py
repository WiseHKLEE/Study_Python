#filter 함수 사용하지 않고 양수값만 리턴하는 함수

def positive(numberList):
    result = []
    for num in numberList:
        if num > 0:
            result.append(num)
    return result
print(positive([1,-3,2,0,-5,6]))



#filter 기능 사용하여 양수값만 리턴
def filtertest1(x):
    return x > 0
print(list(filter(filtertest1,[1,-3,2,0,-5,6])))

#lambda를 이용하여 Filter
print(list(filter(lambda x:x>0, [1,-3,2,0,-5,6])))

sum = lambda a,b:a+b  #lambda는 함수를 생성할 때 사용되는 예약어로, def와 동일한 역할. 함수를 한줄로 간결하게 만들때 사용되며 def를 사용해야 할 정도로 복잡하지 않거나,
print(sum(3, 4))      #def를 사용할 수 없는 곳에 쓰인다.

'''
def sum(a,b):
    return a+b
'''

a = len("python")  #len은 입력값의 길이(요소의 전체 갯수)를 리턴하는 함수
print(a)
b = len([1,2,3])
print(b)
c = len((1,'a'))
print(c)


list1 = list("python")  #list는 반복 가능한 자료형을 입력받아 list로 만들어 리턴하는 함수
print(list1)
list2 = list((1,2,3))
print(list2)