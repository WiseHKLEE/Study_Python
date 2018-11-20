def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a)!=type(b):
        print("더할수 있는것이 아닙니다.")
        return
    else:
        result = sum(a,b)
        return result



if __name__ == "__main__":    #직접 이 파일을 실행시켰을때만 해당 line이 참이되어 하위 문장들이 수행된다. 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할때는 거짓이 되어 사용 불가
    print(safe_sum('a',1))
    print(safe_sum(1,4))
    print(sum(10,10.4))
