lookup = {'R':(1,0), 'L':(-1,0),'U':(0,1),'D':(0,-1)}
cnt = 0
size = 0
wires = []
for row in open('test').readlines():
    data = row.split(',')
    wires.append(set())
    x = size
    y = size
    for token in data:
        num = int(token[1:])
        dir = lookup[token[0]]
        for i in range(num):
            x+=dir[0]
            y+=dir[1]
            wires[cnt].add((x,y))
    cnt+=1
for case in range(int(len(wires)/2)):
    common = wires[case*2].intersection(wires[case*2+1])
    print(len(common))
    min = 1000000000000
    res = None
    for i in common:
        if abs(i[0])+abs(i[1])<min:
            min = abs(i[0])+abs(i[1])
            res = i
    print(min,res)
