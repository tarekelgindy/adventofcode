input_file = 'sample1.txt'
input_file = 'input.txt'
square = [[0 for i in range(1001)] for j in range(1001)]
maxx = 0
maxy = 0
for row in open(input_file,'r').readlines():
    sp = row.split()
    corner = [int(x) for x in sp[2][:-1].split(',')]
    size = [int(x) for x in sp[3].split('x')]
    for i in range(size[0]):
        for j in range(size[1]):
            square[corner[0]+i][corner[1]+j] +=1
            maxx = max(maxx,corner[0]+i)
            maxy = max(maxy,corner[1]+j)

res = 0
for i in range(len(square)):
    for j in range(len(square)):
        if square[i][j]>1:
            res+=1
for i in range(maxx+1):
    st=''
    for j in range(maxy+1):
        st+=str(square[i][j])
    print(st)
print(res)

