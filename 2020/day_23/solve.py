tst = '389125467'
tst= '872495136'
tst = [int(tst[i]) for i in range(len(tst))]
next_element = {}
reverse_lookup_dict = {}
for i in range(len(tst)-1):
    next_element[tst[i]] = tst[i+1]
next_element[tst[-1]] = len(tst)+1
size = 1000000
for i in range(len(tst)+1,1000000):
    next_element[i] = i+1
next_element[1000000] = tst[0]
t = 0
curr=tst[0]
while t<10000000:
    if t%100000 == 0:
        print(t,curr,flush=True)
    out = []
    nxt=curr
    for i in range(3):
        out.append(next_element[nxt])
        nxt = next_element[nxt]
    minus = 0
    m_cnt = 0
    while m_cnt !=1:
        minus+=1
        if curr-minus == 0:
            minus = curr-size
        if curr-minus in out:
            continue
        m_cnt+=1
    dest = curr-minus
    old_seq = next_element[out[-1]]
    next_element[curr] = old_seq

    next_element[out[-1]] = next_element[dest]
    next_element[dest] = out[0]

    curr = next_element[curr]
    t+=1
v1 = next_element[1]
v2 = next_element[v1]
print(v2*v1)
