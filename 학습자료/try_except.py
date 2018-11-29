try:
    4/0
except ZeroDivisionError as e:  #try 블록 수행 중 오류가 발생할때 except문에 정해놓은 오류이름(ZeroDivisionError)와 동일할 경우에 except 수행
    print(e)