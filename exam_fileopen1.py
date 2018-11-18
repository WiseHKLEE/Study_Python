with open ('sample.txt','r') as f:
    lines = f.readlines()

total = 0
for line in lines:
    score = int(line)
    total += score

average = total / len(lines)

with open ('result.txt', 'w') as f:
    f.write(str(average))