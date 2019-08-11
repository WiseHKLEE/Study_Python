import sys

while True:
    a,b = map(int,sys.stdin.readline().split())
    if a >= 10 or b >= 10:
        break
    print(a+b)