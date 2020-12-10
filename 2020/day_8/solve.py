data = []
res = 0
res2 = 0
#for row in open('test.txt').readlines():
for row in open('input.txt').readlines():
    data.append(row.strip())

pos = 0
acc=0
seen = set()
while 1:
    entry = data[pos]
    vals = entry.split()
    if pos in seen:
        break
    seen.add(pos)
    if vals[0]=='nop':
        pos+=1
    if vals[0]=='acc':
        if vals[1][0] =='+':
            acc+=int(vals[1][1:])
        if vals[1][0] =='-':
            acc-=int(vals[1][1:])
        pos+=1
    if vals[0]=='jmp':
        if vals[1][0] =='+':
            pos+=int(vals[1][1:])
        if vals[1][0] =='-':
            pos-=int(vals[1][1:])
print(acc)
for i in range(len(data)):
    pos = 0
    acc=0
    seen = set()
    ok = True
    data2 = []
    for d in data:
        data2.append(d)
    if 'jmp' in data2[i]:
        data2[i] = 'nop +0'
    else:
        continue
    while 1:
        if pos >= len(data2) or pos < 0:
            break
        entry = data2[pos]
        vals = entry.split()
        #print(vals)
        if pos in seen:
            ok=False
            break
        seen.add(pos)
        if vals[0]=='nop':
            pos+=1
        if vals[0]=='acc':
            if vals[1][0] =='+':
                acc+=int(vals[1][1:])
            if vals[1][0] =='-':
                acc-=int(vals[1][1:])
            pos+=1
        if vals[0]=='jmp':
            if vals[1][0] =='+':
                pos+=int(vals[1][1:])
            if vals[1][0] =='-':
                pos-=int(vals[1][1:])
    if ok:
        print(acc)


