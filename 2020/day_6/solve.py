good = 0
good2 = 0
data = []
#for row in open('test.txt'):
for row in open('input.txt'):
    data.append(row.strip())


all_s = set()
all_s2=[]
res = 0
res2 = 0
for row in data:
    if len(row)==0:
        res+=len(all_s)
        ret = all_s2[0]
        for i in range(1,len(all_s2)):
            ret = ret.intersection(all_s2[i])
        res2+=len(ret)
        #print(all_s2)
        all_s=set()
        all_s2=[]
        continue
    tmp=set()
    for i in row:
        tmp.add(i)
    all_s2.append(tmp)
res+=len(all_s)
ret = all_s2[0]
for i in range(1,len(all_s2)):
    ret = ret.intersection(all_s2[i])
res2+=len(ret)

print(res)
print(res2)

