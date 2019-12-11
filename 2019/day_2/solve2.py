for row in open('input.txt').readlines():
    data = row.split(',')
    for i in range(len(data)):
        data[i] = int(data[i])
    orig_data = []
    for i in range(len(data)):
        orig_data.append(data[i])
    res = 19690720
    for i in range(100):
        for j in range(100):
            if j > len(orig_data):
                break
            data = []
            for k in range(len(orig_data)):
                data.append(orig_data[k])
            data[1] = i
            data[2] = j
            pos = 0
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
            if data[0] == res:
                print(i,j,100*i+j)
                break
            #print(data[0])
