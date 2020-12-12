import math
data = []
for row in open('input.txt').readlines():
#for row in open('test.txt').readlines():
    data.append(row.strip())

x=0
y=0
wayx=10
wayy=1
x2=0
y2=0
facing = 0
for row in data:
    action = row[0]
    value = int(row[1:])
    if action == 'N':
        y+=value
        wayy+=value
    if action == 'S':
        y-=value
        wayy-=value
    if action == 'E':
        x+=value
        wayx+=value
    if action == 'W':
        x-=value
        wayx-=value
    if action == 'R':
        facing -= value
        for cnt in range(int(value/90)):
            tmp = wayx
            wayx=wayy
            wayy=-1*tmp
    if action == 'L':
        facing +=value
        for cnt in range(int(value/90)):
            tmp = wayx
            wayx=-1*wayy
            wayy=tmp
    facing =facing %360
    if action=='F':
        x += int(value*math.cos(facing*math.pi/180))
        y+= int(value*math.sin(facing*math.pi/180))
        x2+=wayx*value
        y2+=wayy*value
print(abs(x)+abs(y))
print(abs(x2)+abs(y2))
