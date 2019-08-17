result = []

for i in range(9):
    result.append(int(input()))

print(max(result))
print(result.index(max(result))+1)
