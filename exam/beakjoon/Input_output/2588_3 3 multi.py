x = int(input())
y = int(input())

a = y//100
b = (y%100)//10
c = (y%100)%10

print(c*x)
print(b*x)
print(a*x)
print(x*y)