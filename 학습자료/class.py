#클래스에 의해서 생성된 객체들은 다른 객체들과 달리 완전히 다른 저장공간을 가지고 독립적으로 동작한다.
#클래스는 똑같은 무언가를 계속해서 만들어낼수 있는 일종의 설계도면 같은것.

class HousePark:
    lastname = "박"
    def __init__(self,name): #instance를 만들때 항상 실행되는 함수
        self.fullname = self.lastname + name #self : instance의 변수와 함수의 값을 연결해주는 것

    def travel(self,where):
        print("%s, %s여행을 가다." %(self.fullname, where))

    def love(self,other):
        print("%s, %s 사랑에 빠졌네" %(self.fullname, other.fullname))

    def __add__(self, other): #연산자 오버로딩 : 연산자(+ - / * ...)를 객체끼리 사용할 수 있게하는 기법
        print("%s, %s 결혼했네" %(self.fullname, other.fullname))

    def fight(self, other):
        print("%s, %s 싸우네" %(self.fullname, other.fullname))

    def __sub__(self, other): #연산자 오버로딩 : 연산자(+ - / * ...)를 객체끼리 사용할 수 있게하는 기법
        print("%s, %s 이혼했네" %(self.fullname, other.fullname))




class HouseKim(HousePark): #클래스의 상속
    lastname = "김"
    def travel(self,where,day): #메소드 오버라이딩 : 메소드 이름을 동일하게 하여 재 구현하는것.
        print("%s, %s여행 %d일 가네." %(self.fullname, where, day))

pey = HousePark("응용")  #instance. 즉, 클래스에 의해서 만들어진 피조물
juliet = HouseKim("줄리엣")
pey.travel("부산")
juliet.travel("부산", 3)
pey.love(juliet)
pey + juliet
pey.fight(juliet)
pey - juliet


