def update(input_matrix):
    output_matrix = []
    for i in range(len(input_matrix)):
        toadd = []
        for j in range(len(input_matrix[i])):
            toadd2 = []
            for k in range(len(input_matrix[i][j])):
                active_neighbors = 0
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        for z in [-1,0,1]:
                            if z==0 and y==0 and x==0:
                                continue
                            if i+x >=0 and i+x<len(input_matrix) and j+y >=0 and j+y<len(input_matrix[i]) and k+z >=0 and k+z <len(input_matrix[i][j]) and input_matrix[i+x][j+y][k+z] == '#':
                                active_neighbors +=1
                if active_neighbors == 3 and input_matrix[i][j][k] == '.':
                    toadd2.append('#')
                if active_neighbors != 3 and input_matrix[i][j][k] == '.':
                    toadd2.append('.')
                if (active_neighbors == 3 or active_neighbors==2) and input_matrix[i][j][k] == '#':
                    toadd2.append('#')
                if not(active_neighbors == 3 or active_neighbors==2) and input_matrix[i][j][k] == '#':
                    toadd2.append('.')
            toadd.append(toadd2)
        output_matrix.append(toadd)
    return output_matrix



data = []
#for row in open('test.txt'):
for row in open('input.txt'):
    data.append(row.strip())

current_state = []

print(data)
max_size = 15
for i in range(-1*max_size,max_size):
    toadd = []
    for j in range(-1*max_size,max_size):
        toadd2 = []
        for k in range(-1*max_size,max_size):
            if k==0 and i>=0 and i<len(data) and j>=0 and j<len(data[i]):
                toadd2.append(data[i][j])
            else:
                toadd2.append('.')
        toadd.append(toadd2)
    current_state.append(toadd)


for t in range(6):
    next_matrix = update(current_state)
    current_state = next_matrix
    """
    print(t)
    for k in range(len(current_state)):
        print('z=',k-max_size)
        for i in range(len(current_state)):
            for j in range(len(current_state[i])):
                print(current_state[i][j][k],end='')
            print()
    """
res = 0
for i in range(len(current_state)):
    for j in range(len(current_state)):
        for k in range(len(current_state)):
            if current_state[i][j][k] == '#':
                res+=1
    
print(res)

