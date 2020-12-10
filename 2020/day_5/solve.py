good = 0
good2 = 0
data = []
#for row in open('test.txt'):
for row in open('input.txt'):
    data.append(row.strip())

all_vals = set()
max_val = 0
for row in data:
    curr=64
    val = 0
    for i in range(7):
        if row[i]=='B':
            val+=curr
        curr=curr/2
    val*=8
    curr=4
    for i in range(3):
        if row[7+i]=='R':
            val+=curr
        curr=curr/2
    all_vals.add(val)
    if val > max_val:
        max_val=val
print(max_val)
all_vals2 = sorted(list(all_vals))
first = int(all_vals2[0])
last = int(all_vals2[-1])
for i in range(first,last+1):
    if not i in all_vals:
        print(i)

        

    
