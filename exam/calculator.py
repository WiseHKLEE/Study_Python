class Calculator:
    def __init__(self, number):
        self.number = number

    def sum(self):
        result = 0
        for i in self.number:
            result += i
        return result

    def avg(self):
        result = 0
        for i in self.number:
            result += i
        return result / len(self.number)

if __name__ == "__main__":
    cal1 = Calculator([1,2,3,4,5])
    print(cal1.sum())
    print(cal1.avg())

    cal2 = Calculator([6,7,8,9,10])
    print(cal2.sum())
    print(cal2.avg())
