'''
#map함수를 이용하지 않고 반복가능한 자료형을 입력받아 처리하는 방법
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)
'''


def two_times(x):return x*2
a = list(map(two_times, [1,2,3,4]))
print(a)

'''
#map 진행 순서
1. list의 첫번째 요소인 1이 two_times 함수의 입력값으로 들어가서, 1*2 과정을 거쳐 2가 된다.ㅣ
2. 이런식으로 4개의 list요소값이 모두 수행되면 [2,4,6,8] 이 리턴
'''


b = list(map(lambda x:x*2, [1,2,3,4]))
print(b)