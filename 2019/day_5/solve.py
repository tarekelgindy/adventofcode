for row in open('input.txt').readlines():
    data = row.split(',')
    for i in range(len(data)):
        data[i] = int(data[i])
    pos = 0
    #data[1]=12
    #data[2]=2
    while pos < len(data):
        print(data[pos])
        inc = None
        if data[pos] == 99:
            break
        elif data[pos] == 1:
            data[data[pos+3]] = data[data[pos+1]]+data[data[pos+2]]
            inc = 4
        elif data[pos] == 2:
            data[data[pos+3]] = data[data[pos+1]]*data[data[pos+2]]
            inc = 4
        elif data[pos] == 3:
            data[data[pos+1]] = 1
            inc = 2
        elif data[pos] == 4:
            print(data[data[pos+1]])
            inc = 2
        elif len(str(data[pos]))>2:
            entry = str(data[pos])
            code = int(entry[-2:])
            inc = len(entry)-2
            cnt = 1
            if code == 1:
                res = 0
            if code ==2:
                res = 1
            done = False
            for i in range(-3,-1*len(entry),-1):
                val = 0
                if entry[i] == 0:
                    val = data[data[pos+cnt]]
                if entry[i] == 1:
                    val = data[pos+cnt]
                if code == 2:
                    res*=val
                if code == 1:
                    res += val
                if code == 99:
                    done = True
                    break
                if code == 4:
                    print(val)
                cnt +=1
            if done:
                break

        else:
            print('unrecognized')
        pos+=inc
    print(data)
    print(data[0])
