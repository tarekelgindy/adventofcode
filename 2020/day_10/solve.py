data = []
res = 0
res2 = 0
for row in open('input.txt').readlines():
#for row in open('input.txt').readlines():
    data.append(int(row.strip()))

data = sorted(data)
curr=0
res =0
one =0
three=0
diffs = []
cnt = 0
for i in data:
    diffs.append(i-curr)
    print(i-curr)
    if i-curr==1:
        one+=1
    if i-curr==3:
        three+=1
    curr=i
    cnt+=1
three+=1
print(one*three)
res = 1
count = 0
pascal=[[0,0,0] for  i in range(200)]
pascal[1]=[1,0,0]
pascal[2]=[1,1,0]
for i in range(3,200):
    pascal[i][0]=1
    for j in range(1,3):
        pascal[i][j]=pascal[i-1][j]+pascal[i-1][j-1]


for i in range(len(diffs)):
    if diffs[i] ==1:
        count+=1
    else:
        print(count)
        if count>0:
            res*=sum(pascal[count])
        count=0
if count>0:
    res*=sum(pascal[count])
print(res)


