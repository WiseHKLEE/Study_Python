a, b, c = map(int, input().split()) #map을 이용하여 iterable 데이터를 인자로 받아 결과를 List 형태로 반환해준다.
                                    #split을 이용하여 data 구별
result1 = (a+b)%c
result2 = (a%c + b%c)%c
result3 = (a*b)%c
result4 = (a%c * b%c)%c

print(result1)
print(result2)
print(result3)
print(result4)