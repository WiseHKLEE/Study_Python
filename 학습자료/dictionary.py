'''
dictionary 주의사항
-- key값은 고유한 값이므로 중복되는 값을 설정해 놓으면 안됨.
if 중복이 된다면 하나만 적용되고, 나머지는 제외

key값으로 list는 쓸수 없음. Tuple은 Key값으로 사용 가능하다.
key값은 값이 변할 수 없다는 전체하에 Type을 설정.

dict() 함수
'''

aa = dict() #항목(item)없는 Dictionary를 만든다.
print(aa)

aa['one'] = '첫번째'
print(aa)


# key list를 만드는 함수
bb = {'name':'홍길동','hp':'010-1234-1234','age':24}
keylist = bb.keys() #Return 객체는 dict_keys
print(keylist)

for key in bb.keys(): #dict_keys 객체의 각 요소값을 출력
    print(key)

keylist1 = list(bb.keys()) #dict_keys 객체를 list로 변환
print(keylist1)

#value list를 만드는 함수(values)
valuelist = bb.values() #return 객체는 dict_values
print(valuelist)

#key와 value 한쌍을 만드는 함수(items)
itemlist = bb.items() #return 객체는 dict_items
print(itemlist)

#key:value 모두 삭제는 clear()
#bb.clear()
#print(bb)

#key값을 이용하여 value값 얻어오기(get)
age = bb.get('age')
print(age)

age = bb['age'] #get함수를 이용하지 않고 사용하는 방법
print(age)

'''
gender = bb['gender'] #key값이 존재하지 않으면 에러 출력
print(gender)
'''

#get 함수는 해당 key값이 존재하지 않을 경우에는 none값 return
gender = bb.get('gender')
print(gender)

#dictionary에 key값이 없을 경우, default값을 주는 방법
gender = bb.get('gender','원하는값')
print(gender)

#dictionary에 해당 key가 존재하는지 알아보기
confirm_bb = 'gender' in bb
print(confirm_bb)

confirm_bb='name' in bb
print(confirm_bb)

#pop함수를 이용해서 value값을 가져오기 : dictionary의 항목을 제거
m = bb.pop('name')
print(m)
print('pop함수 이수의 dictionary')
print(bb)

bb['name'] = '홍길동'
print(bb)

m = bb.pop('gender', '없음')
print(m)

length = len(bb) #dictionary의 항목 count
print(length)
