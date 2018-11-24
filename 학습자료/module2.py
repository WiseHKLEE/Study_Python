PI = 3.141592
class Math: #다른 모듈에서 해당 Class 사용하려면 (모듈명).(클래스명())을 사용한다.
    def solv(self, r):
        return PI * (r ** 2)

def sum(a,b):
    return a+b

if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI,4.4))