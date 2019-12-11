input_file = 'sample2.txt'
input_file = 'input.txt'
all_strs = []
for row in open(input_file,'r').readlines():
    all_strs.append(row)
for ii in range(len(all_strs)):
    row1 = all_strs[ii]
    for jj in range(ii+1,len(all_strs)):
        row2 = all_strs[jj]
        if len(row1)!=len(row2):
            continue
        cnt = 0
        pos = 0 
        for i in range(len(row1)):
            if row1[i]!=row2[i]:
                pos = i
                cnt+=1
        if cnt ==1:
            res = row1[:pos]+row1[pos+1:]
            print(row1.strip(),row2.strip(),res.strip())

