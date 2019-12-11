for row in open('input.txt').readlines():
    data = row.split(',')
    for i in range(len(data)):
        data[i] = int(data[i])
    pos = 0
    data[1]=12
    data[2]=2
    while pos < len(data):
        if data[pos] == 99:
            break
        elif data[pos] == 1:
            data[data[pos+3]] = data[data[pos+1]]+data[data[pos+2]]
        elif data[pos] == 2:
            data[data[pos+3]] = data[data[pos+1]]*data[data[pos+2]]
        else:
            print('unrecognized')
        pos+=4
    print(data)
    print(data[0])
