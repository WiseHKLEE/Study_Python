n = int(input())
check = n
result = 0
first = 0
second = 0
roof_count = 1

if n < 0 and n > 99:
    exit()

while True:
    first = int(n / 10)
    second = n % 10
    result = first + second
    n = (second * 10) + (result % 10)

    if (check == n):
        break
    else:
        roof_count += 1

print(roof_count)