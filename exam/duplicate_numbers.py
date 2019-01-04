def check_num(s):
    result = []
    for num in s:
        if num not in result:  #변수 s에 있는 값들이 result에 포함되어 있지 않으면 result 항목에 추가
            result.append(s)
        else:
            return False   #변수 s에 있는 값들이 result에 포함되어 있으면 False값 return
    return len(result) == 10  #for 문을 다 돌리고 result의 길이가 10이면 True

print(check_num("0123456789"))
print(check_num("01234"))
print(check_num("01234567890"))
print(check_num("6789012345"))
print(check_num("012322456789"))
