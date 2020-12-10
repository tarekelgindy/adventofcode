data = []
res = 0
res2 = 0
#for row in open('test.txt').readlines():
for row in open('input.txt').readlines():
    data.append(int(row.strip()))

preamble = 25
res = 0
for i in range(preamble,len(data)):
    allowed = set()
    for j in range(i-preamble,i):
        for k in range(i-preamble,i):
            if j==k:
                continue
            allowed.add(data[j]+data[k])
    if data[i] not in  allowed:
        print(data[i])
        res=data[i]
        break
done=False
for i in range(len(data)):
    run = 0
    if done:
        break
    for j in range(i,len(data)):
        run+=data[j]
        if run > res:
            break
        if run==res:
            minval=100000000000000000000
            max_val=-1
            for k in range(i,j+1):
                if data[k]> max_val:
                    max_val=data[k]
                if data[k]< minval:
                    minval=data[k]
            print(minval+max_val)
            done=True
            break

