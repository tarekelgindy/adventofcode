data = []
for row in open('input.txt'):
    val = int(row)
    data.append(val)
for i in data:
    for j in data:
        if i+j==2020:
            print(i*j)
for i in data:
    for j in data:
        for k in data:
            if i+j+k==2020:
                print(i*j*k)
