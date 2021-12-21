from collections import Counter

input = []
with open('./day_3.txt', 'r') as f:
    for i in f.readlines():
        input.append(str(i.strip()))

gamma = ''
epsilon = ''
count = Counter([0,1])


for i in range(len(input[0])):
    for j in input:
        count[int(j[i])] += 1

    c = count.most_common(2)
    gamma+=str(c[0][0])
    epsilon+=str(c[1][0])
    count = Counter([0, 1])

print(int(gamma, 2) * int(epsilon, 2))
print('---------------')
###############################################

def recursive_f(data, idx, o_c):
    counnt = Counter([0,1])
    for j in data:
        counnt[int(j[idx])] += 1
    cc = counnt.most_common(2)
    if int(cc[0][1]) == int(cc[1][1]):
        g = str(o_c)
    elif bool(int(o_c)):
        g = str(cc[0][0])
    else:
        g = str(cc[1][0])

    new_data = [k for k in data if k[idx] == g]
    idx = idx+1

    if len(new_data) == 1:
        return new_data
    else:
        return recursive_f(new_data,idx, o_c)


o2 = input.copy()
co2 = input.copy()
print(int(recursive_f(o2,0,'1')[0],2) * int(recursive_f(co2,0,'0')[0],2))
