input = []
with open('./day1.txt', 'rb') as f:
    for i in f.readlines():
        input.append(int(i.strip()))

count = 0
s = sum(input[:3])
for i in range(1, len(input)):
    ss = sum(input[i:i+3])
    if ss > s:
        count+=1
    s = ss
print(count)

for (j,k) in zip(input[3:], input[:-3]):
    print(j,k)