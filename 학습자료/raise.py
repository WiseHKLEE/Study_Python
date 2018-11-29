class Bird:
    def fly(self):
        raise NotImplementedError #Bird 클래스를 상속받는 자식클래스가 반드시 fly라는 함수를 구현하도록 해야할 때 사용된다.



class Eagle(Bird): #bird 클래스를 상속받는 Eagle클래스가 fly함수를 구현하지 않았기 때문에, bird 클래스의 fly 함수가 호출되며, raise문에 의해 NotImplemented Error 출력
    pass
eagle = Eagle()
eagle.fly()


'''
class Eagle(Bird):
    def fly(self):  #NotImplementedError를 발생시키지 않으려면 Eagle에 fly함수를 반드시 구현해야한다.
        print("very fast")

eagle = Eagle()
eagle.fly()
'''