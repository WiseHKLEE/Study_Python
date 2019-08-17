a = int(input())
b = int(input())
c = int(input())

result = []

n = int(a * b * c)
n = str(n)

for i in range(0,10):
    print(n.count(str(i)))
