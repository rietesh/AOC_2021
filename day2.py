input = []
with open('./day2.txt', 'r') as f:
    for i in f.readlines():
        input.append(tuple(i.split()))

(h,d,a) = (0,0,0)
for i in input:
    if i[0][0] == 'f':
        h += int(i[1])
        d += a*int(i[1])
    elif i[0][0] == 'd':
        a += int(i[1])
    elif i[0][0] == 'u':
        a -= int(i[1])
    # print(i,h,d)
print(h*d)
