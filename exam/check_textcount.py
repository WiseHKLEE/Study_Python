import sys

n = sys.argv[1]
#xxxyyzzzz가 들어갔을 경우
def compress_string(s):
    a = ""
    cnt = 0
    result = ""
    for c in s:
        if c != a:   # 들어온 값이 변수 a와 동일하지 않은지?
            a = c    # 동일하지 않다면 들어온 값은 변수 a와 동일한 값으로 변경
            if cnt:  # cnt가 0이 아니라면 result는 result+str(cnt)
                result += str(cnt)
            result += c #result = result + c
            cnt = 1
        else:
            cnt += 1
    if cnt: # cnt가 0이 아니라면 result는 result+str(cnt)
        result += str(cnt)  #마지막 문자의 반복횟수를 처리하는 동작
    return result

print(compress_string(n))