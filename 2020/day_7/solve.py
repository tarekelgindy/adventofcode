data = []
lookup = {}
lookup_nums = {}
reverse_lookup = {}
#for row in open('test2.txt').readlines():
for row in open('input.txt').readlines():
    row2=row.replace('bags.','bag')
    row2=row2.replace('bags,','bag')
    row2=row2.replace('bags','bag')
    row2=row2.replace('bag,','bag')
    row2=row2.replace('bag.','bag')
    s = row2.split('bag')
    key = s[0].strip()
    value = set()
    value2 = set()
    if not ('no other' in s[1]):
        for i in range(1,len(s)-1):
            val = s[i].strip().replace('contain','')
            val2 = val.split()
            number = int(val2[0])
            name = ' '.join(val2[1:])
            value.add(name)
            value2.add((name,number))
    lookup[key] = value
    lookup_nums[key] = value2
for element in lookup:
    value = set()
    for element2 in lookup:
        if element in lookup[element2]:
            value.add(element2)
    reverse_lookup[element] = value
queue = []
res = -1
seen = set()
queue.append('shiny gold')
while len(queue) > 0:
    curr = queue.pop(0)
    if curr in seen:
        continue
    print(curr)
    seen.add(curr)
    res+=1
    for element in reverse_lookup[curr]:
        queue.append(element)
queue = []
res2 = -1
queue.append(('shiny gold',1))
while len(queue) > 0:
    curr = queue.pop(0)
    res2+=curr[1]
    for i in range(curr[1]):
        for element in lookup_nums[curr[0]]:
            queue.append(element)

print(res)
print(res2)

