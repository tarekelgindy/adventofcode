def gcd(a,b):
    if b>a:
        tmp = b
        b = a
        a = tmp
    while b !=0:
        t = b
        b = a%b
        a = t
    return a
def can_see(matrix,i,j,k,l):
    diff1 = i-k
    diff2 = j-l
    cnt = gcd(abs(diff1),abs(diff2))
    val1 = int(diff1/cnt)
    val2 = int(diff2/cnt)
    #print(val1,val2,cnt,diff1,diff2)
    pos1 = k
    pos2 = l
    for nn in range(cnt-1):
        pos1 += val1
        pos2 += val2
    #    print(pos1,pos2,k,l)
        if not matrix[pos1][pos2]:
            return False
    return True

data = []
matrix = []

for row in open('data.txt').readlines():
    if len(row)==0:
        continue
    data.append(row.strip())
tot=0
for row in data:
    newrow = []
    for i in range(len(row)):
        if row[i] == '.':
            newrow.append(True)
        else:
            newrow.append(False)
            tot+=1
    matrix.append(newrow)
solution = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if not matrix[i][j]:
            for k in range(len(matrix)):
                for l in range(len(matrix[0])):
                    if not matrix[k][l] and not (i==k and j==l):
                        res = can_see(matrix,i,j,k,l)
                        if res:
                            solution[i][j]+=1
                        else:
                            if i == 3 and j == 6:
                                print(solution[i][j],k,l)
print(solution)
maxx = 0
pos = None
for i in range(len(solution)):
    for j in range(len(solution[0])):
        if solution[i][j] > maxx:
            maxx = solution[i][j]
            pos = (i,j)
print(maxx)
print(pos[0],pos[1])
count = 0
#Fix ordering
for j in range(pos[1],len(matrix[0]),1):
    for i in range(0,pos[0]):
        #print(pos[0],i,pos[1],j)
        if not matrix[i][j] and can_see(matrix,i,j,pos[0],pos[1]):
            matrix[i][j] = True
            count +=1
            print(i,j)
        elif not matrix[i][j]:
            ii = i
            jj = j
            diff1 = pos[0]-i
            diff2 = pos[1] -j
            cnt = gcd(abs(diff1), abs(diff2))
            v1 = int(diff1/cnt)
            v2 = int(diff2/cnt)
            for nn in range(cnt-1):
                ii = i+v1
                jj = j+v2
                if can_see(matrix,ii,jj,pos[0],pos[1]):
                    matrix[ii][jj] = True
                    count +=1
                    print(ii,jj,'ss')
                    break
            break
