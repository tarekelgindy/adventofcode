lookup = {'R':(1,0), 'L':(-1,0),'U':(0,1),'D':(0,-1)}
cnt = 0
size = 0
wires = []
lookups = []
for row in open('test').readlines():
    data = row.split(',')
    wires.append(set())
    lookups.append({})
    x = size
    y = size
    running = 1
    for token in data:
        num = int(token[1:])
        dir = lookup[token[0]]
        for i in range(num):
            x+=dir[0]
            y+=dir[1]
            lookups[cnt][(x,y)]=running
            wires[cnt].add((x,y))
            running+=1
    cnt+=1
for case in range(int(len(wires)/2)):
    common = wires[case*2].intersection(wires[case*2+1])
    print(len(common))
    min = 1000000000000
    res = None
    for i in common:
        if lookups[case*2][i] + lookups[case*2+1][i]<min:
            min = lookups[case*2][i] + lookups[case*2+1][i]
            res = i
    print(min,res)
