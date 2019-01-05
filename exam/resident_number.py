data = """
park 800905-1049118
kim 700905-1059119
"""

result = []
for line in data.split("\n"): #data의 값을 line별로 분리
    word_result=[] #line별 Data 합산용 변수
    for word in line.split(" "): #문자열의 값을 공란(space) 단위로 분리 
        if len(word) == 14 and word[:6].isdigit() and word[7:14].isdigit():  #길이가 14이면서 6번째 자리 까지 and 7~14번째가 숫자일 경우
            word = word[:6] + "-" + "*******"
        word_result.append(word)  #word값을 word_result에 추가
    result.append(" ".join(word_result)) #이름과 주민번호가 리스트 항목별로 기재되어있는것을 한칸의 공란을 주어 합병처리
print("\n".join(result))  #for문을 돌려서 나온값별로 줄바꿈처리하여 출력 



#정규 표현식을 써서 사용한 경우

import re

data = """
park 800905-1049118
kim 700905-1059119
"""


pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))