n,x = map(int,input().split())
a = list(map(int,input().split()))
total = []

for i in range(n):
    if a[i]<x:
        total.append(a[i])

for item in total:
    print(item, end=' ')