data = []
for row in open('input.txt'):
#for row in open('test.txt'):
    data.append(row.strip())
res = []
adder = [1,3,5,7,1]
for idx in range(len(adder)):
    pp = adder[idx]
    cnt = 0
    y=0
    cc = 0
    for row in data:
        if row[y%len(row)]=='#':
            if not(idx==4 and cc%2==1):
                cnt+=1
        if idx==4 and cc%2==1:
            y-=pp
        y+=pp
        cc+=1
    print(cnt)
    res.append(cnt)
ret = 1
for i in res:
    ret*=i
print(ret)

