tst = '389125467'
tst= '872495136'
tst = [int(i) for i in tst]
t = 0
pos = 0
while t<100:
    curr = tst[pos]
    out = []
    for i in range(1,4):
        out.append(tst[(pos+i)%len(tst)])
    minus = 0
    m_cnt = 0
    while m_cnt !=1:
        minus+=1
        print('m',curr-minus)
        if curr-minus == 0:
            minus = curr-len(tst)
        if curr-minus in out:
            continue
        m_cnt+=1

    dest = curr-minus
    nxt = []
    for i in range(len(tst)):
        if tst[i] in out:
            continue
        nxt.append(tst[i])
        if tst[i] == dest:
            for j in out:
                nxt.append(j)
    print(nxt)
    for i in range(len(nxt)):
        if nxt[i] == curr:
            pos=(i+1)%len(nxt)
            break
    tst=nxt
    t+=1

res = ''
pos = 0
for i in range(len(tst)):
    if tst[i] ==1:
        pos=(i+1)%len(tst)
        break
for i in range(len(tst)-1):
    res=res+str(tst[pos])
    pos=(pos+1)%len(tst)
print(res)





