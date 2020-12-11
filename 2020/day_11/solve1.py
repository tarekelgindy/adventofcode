data = []
res = 0
res2 = 0
dirs = [[i,j] for i in [0,-1,1] for j in [0,-1,1]]
dirs = dirs[1:]
#for row in open('test.txt').readlines():
for row in open('input.txt').readlines():
    data.append(row.strip())

res = 0
while True:
    orig_data = [[] for i in range(len(data))]
    next_data = [[] for i in range(len(data))]
    next_data2 = [[] for i in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data[i])):
            next_data[i].append(data[i][j])
            orig_data[i].append(data[i][j])
    for i in range(len(data)):
        for j in range(len(data[i])):
            count = 0
            for d in dirs:
                ii = i+d[0]
                jj = j +d[1]
                if ii<len(data) and ii>=0 and jj<len(data[i]) and jj>=0 and data[ii][jj] =='#':
                    count+=1
                if count == 0 and data[i][j] =='L':
                    next_data[i][j]='#'
                    changed=True
                else:
                    next_data[i][j]=data[i][j]

    for i in range(len(data)):
        for j in range(len(data[i])):
            next_data2[i].append(next_data[i][j])
    for i in range(len(data)):
        for j in range(len(data[i])):
            count = 0
            for d in dirs:
                ii = i+d[0]
                jj = j +d[1]
                if ii<len(data) and ii>=0 and jj<len(data[i]) and jj>=0 and next_data[ii][jj] =='#':
                    count+=1
                if count >= 4 and next_data[i][j] =='#':
                    next_data2[i][j]='L'
                    changed=True
                else:
                    next_data2[i][j]=next_data[i][j]
    data = [[] for i in range(len(next_data))]
    for i in range(len(next_data2)):
        for j in range(len(next_data2[i])):
            data[i].append(next_data2[i][j])
    res+=1

    changed=False
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j]!=orig_data[i][j]:
                changed=True
    if not changed: 
        break
    
#    for i in data:
#        print(''.join(i))
#    print()

res=0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]=='#':
            res+=1
print(res)


