cnt=0
all_memory = {}
all_memory_2 = {}
#for row in open('test2.txt').readlines():
maxx = 0
for row in open('input.txt').readlines():
    if row.startswith('mask'):
        mask=list(row.strip().split()[2])
    else:
        row2=row.replace('[',' ').replace(']',' ')
        sp = row2.split()
        mem = int(sp[1])
        mem2 = mem
        val = int(sp[3])
        val2=val
        curr = [0 for i in range(36)]
        curr2 = [0 for i in range(36)]
        for i in range(35,-1,-1):
            if int(val/(2**i)) >0:
                curr[35-i]=1
                val-= (2**i)
            if int(mem2/(2**i)) >0:
                curr2[35-i]=1
                mem2-= (2**i)
        xcnt = 0
        for i in range(36):
            if mask[i]!='X':
                curr[i]=int(mask[i])
            if mask[i] == '1':
                curr2[i] =1
            if mask[i] == 'X':
                xcnt+=1
                curr2[i]='X'
        if xcnt > maxx:
            maxx=xcnt
        binary = 1
        local_mem=0
        for i in range(35,-1,-1):
            if curr2[i] !='X':
                local_mem+=binary*curr2[i]
            binary*=2

        all_local_mem = [local_mem] #this blows it up exponentially but at most 9 X values in input -> max 512 total
        binary = 1
        for i in range(35,-1,-1):
            if curr2[i] =='X':
                next_list = []
                for existing_mem in all_local_mem:
                    next_value = existing_mem+binary
                    next_list.append(next_value)
                all_local_mem.extend(next_list)
            binary*=2

        for i in all_local_mem:
            all_memory_2[i] = val2
        all_memory[mem] = curr
result =0
for _,curr in all_memory.items():
    binary = 1
    for i in range(35,-1,-1):
        result+=binary*curr[i]
        binary*=2

result2=0
for _,curr in all_memory_2.items():
    result2+=curr
print(result)
print(result2)
