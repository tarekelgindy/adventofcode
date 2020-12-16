data = []
res = 0
res2 = 0
valid_ranges = set()
valid_map = {}
entry_count =0
total_invalid = 0
good_tickets = []
my_ticket = None
for row_orig in open('input.txt').readlines():
#for row_orig in open('test2.txt').readlines():
    row=row_orig.strip()
    if len(row)==0:
        entry_count+=1
        continue
    if entry_count == 0:
        element = row.split(':')[0]
        sp = row.split(':')[1].strip().split()
        range1 = (int(sp[0].split('-')[0]),int(sp[0].split('-')[1]))
        range2 = (int(sp[2].split('-')[0]),int(sp[2].split('-')[1]))
        valid_ranges.add(range1)
        valid_ranges.add(range2)
        valid_map[element] = (range1,range2)
    if entry_count == 2 or entry_count==1:
        if 'ticket' in row:
            continue
        if entry_count==1:
            my_ticket=row.split(',')
        elements = map(int,row.split(','))
        ticket_good = True
        for i in elements:
            good=False
            for j in valid_ranges:
                if i>=j[0] and i<=j[1]:
                    good=True
                    break
            if not good:
                total_invalid+=i
                ticket_good=False
        if ticket_good:
            good_tickets.append(row)

print(total_invalid)

allowed_names = []
for i in map(int,good_tickets[0].split(',')):
    allowed_nxt = set()
    for i in valid_map:
        allowed_nxt.add(i)
    allowed_names.append(allowed_nxt)

for row in good_tickets:
    cnt = 0
    for i in map(int,row.split(',')):
        allowed_names_v2 = set()
        for j in allowed_names[cnt]:
            if (i>=valid_map[j][0][0] and i<=valid_map[j][0][1]) or (i>=valid_map[j][1][0] and i<=valid_map[j][1][1]):
                allowed_names_v2.add(j)
        allowed_names[cnt] = allowed_names_v2

        cnt+=1
current_count = 0
result = {}
while current_count < len(allowed_names):
    for i in range(len(allowed_names)):
        if len(allowed_names[i]) ==1:
            result[i]=allowed_names[i].pop()
            current_count += 1
            break
    for i in range(len(allowed_names)):
        for j in range(len(allowed_names)):
            if i in result and result[i] in allowed_names[j]:
                allowed_names[j].remove(result[i])

ans=1
for i,j in result.items():
    if 'departure' in j:
        ans*=int(my_ticket[i])
print(result)
print(ans)


        
