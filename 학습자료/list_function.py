'''list 함수들 : 문자열과 같이 list변수명 뒤에 .(함수명) 입력하여 사용

[list에 값을 추가하는 함수]
'''

li = [10,100,1000]
li.append(11)
print(li)

li.append('ab')
print('li')

li.append(['a','b'])
print(li)

#list 정렬함수
li = [1,5,10,2,7]
li.sort()
print(li)

li = ['b','a','f','c']
li.sort() #오름차순순으로 정렬
print(li)

#list 뒤집기 함수
li.reverse() #sort 함수 적용 후, reverse를 사용하게 되면 내림차순이 된다.
print(li)

li = ['b','a','f','c'] #reverse는 내림차순이 아니라 그냥 순서 뒤집는 함수
li.reverse()
print(li)

#요소의 위치를 반환하는 함수
li = ['b','a','f','c']
aa = li.index('a')
print(aa)

''' 없는 값 위치 찾기 시
aa = li.index(1)
print(aa)
'''

#요소 삽입하는 함수
aa = [1,2,3,4]
aa.insert(3,5) #append함수는 제일 뒤에 추가 시키지만, insert함수는 원하는 위치에 추가 가능
print(aa)

#요소 제거하는 함수
cc = [23,12,3,6,5,3]
cc.remove(3) #첫번째 지우고자하는 첫번째 값을 제거
cc.remove(3)
print(cc)

#요소 추출하는 함수
dd = [23,12,3,6,5,3]
aa = dd.pop() #()안에 값이 없을 경우에는 list상의 마지막값을 추출
print(dd)
print(aa)

bb = dd.pop(1) #pop() list의 요소(값)을 끄집어내고, 끄집어낸 요소를 list에서 삭제를 한다.
print(bb)

#요소의 갯수를 파악하기
dd = [23,12,3,6,5,3]
cnt = dd.count(3) #count(요소) 갯수를 구하는 함수
print(cnt)

#list 확장함수
a = [1,2,3]
a.extend([2,3,4,5]) #결과값 : [1,2,3,2,3,4,5]
#a.append([2,3,4,5]) #결과값 : [1,2,3,[2,3,4,5]]
print(a)


a += [2,3,4,5] #a = a+[2,3,4,5], *=(a*=1 --> a=a*1), -=(b-=1 ---> b=b-1)
print(a)
