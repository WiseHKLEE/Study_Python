import random
def random_pop(data):
    number = random.randint(0, len(data)-1)   #random.randint(a,b) : a와 b사이의 정수중 임의의 값 리턴.
    return data.pop(number)                   #data[0] = 1, data[1] = 2, data[2] = 3, ...

def random_choice(data1):
    number = random.choice(data1)             #random.choice는 입력받는 List에서 무작위로 하나를 선택하여 리턴
    data1.remove(number)
    return number

def random_shuffle(data2):                    #random.shuffle은 List항목을 무작위로 섞음
    random.shuffle(data2)
    return data2

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data: print(random_pop(data))
    print("")
    data1 = [1,2,3,4,5]
    while data1: print(random_choice(data1))
    print("")
    data2 = [1,2,3,4,5]
    print(random_shuffle(data2))