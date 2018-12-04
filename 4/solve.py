input_file = 'sample.txt'
input_file = 'input.txt'

all_lines = []
for row in open(input_file,'r').readlines():
    all_lines.append(row)
all_lines = sorted(all_lines)
dic_tot = {}
dic_info = {}
asleep = False
asleep_time = -1
idd = ''
for row in all_lines:
    sp = row.split()
    hour = sp[1][-3:-1]
    if sp[2] == 'Guard':
        idd = sp[3]
    if sp[2] == 'falls':
        asleep = True
        asleep_time = int(hour)
    if sp[2] == 'wakes' and asleep:
        asleep = False
        diff = int(hour) - int(asleep_time)
        if idd not in dic_tot:
            dic_tot[idd] = diff
            value = [0 for i in range(60)]
            for i in range(asleep_time,int(hour)):
                value[i]=1
            dic_info[idd] = value
        else:
            dic_tot[idd] = dic_tot[idd]+diff
            value = dic_info[idd]
            for i in range(asleep_time,int(hour)):
                value[i]+=1
            dic_info[idd] = value

maxsleep = 0
for i in dic_info:
    if dic_tot[i]>maxsleep:
        maxsleep = dic_tot[i]
        maxx = -1
        maxpos = -1
        values = dic_info[i]
        for j in range(len(values)):
            if values[j]>maxx:
                maxx = values[j]
                maxpos = j
        print(i,dic_tot[i],maxpos,maxx,int(i[1:])*maxpos)

        
