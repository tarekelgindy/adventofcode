all_elements = {}
lookup = {'e':(1,0), 'w':(-1,0), 'se':(1,-1), 'sw':(0,-1), 'ne':(0,1), 'nw':(-1,1)}
#for row_orig in open('input.txt').readlines():
for row_orig in open('test.txt').readlines():
    row = row_orig.strip()
    curr = []
    pos = 0
    while pos <len(row):
        if row[pos] == 'e' or row[pos] =='w':
            curr.append(row[pos])
            pos+=1
        else:
            curr.append(row[pos:pos+2])
            pos+=2
    loc = [0,0]
    for i in curr:
        val = lookup[i]
        loc[0]+=val[0]
        loc[1]+=val[1]
    if not tuple(loc) in all_elements:
        all_elements[tuple(loc)] = 0
    all_elements[tuple(loc)]+=1
res = 0
maxx = 0
maxy = 0
dim = 120
grid = [[0 for i in range(-1*dim,dim,1)] for j in range(-1*dim,dim,1)]
for i in all_elements:
    if all_elements[i]%2 == 1:
        res+=1
        grid[i[0]+dim][i[1]+dim] = 1
    if abs(i[0]) > maxx:
        maxx=abs(i[0])
    if abs(i[1]) > maxy:
        maxy = abs(i[1])
print(res) 
size = len(grid)
for t in range(100):
    nxt_grid = [[None for i in range(-1*dim,dim,1)] for j in range(-1*dim,dim,1)]
    for i in range(size):
        for j in range(size):
            cnt = 0
            for _,d in lookup.items():
                ii = i+d[0]
                jj = j+d[1]
                if ii>=0 and ii<size and jj>=0 and jj<size:
                    if grid[ii][jj]==1:
                        cnt+=1
            if grid[i][j] == 1:
                if cnt==0 or cnt >2:
                    nxt_grid[i][j] = 0
                else:
                    nxt_grid[i][j] = 1
            if grid[i][j] == 0:
                if cnt==2:
                    nxt_grid[i][j] = 1
                else:
                    nxt_grid[i][j] = 0
    counter = 0
    for i in range(size):
        for j in range(size):
            grid[i][j] = nxt_grid[i][j]
            if grid[i][j] ==1:
                counter+=1
    print(t+1,counter,flush=True)



