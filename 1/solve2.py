input_file = 'sample1.txt'
input_file = 'input.txt'
f = open(input_file,'r')
tot = 0
all_vals = []
seen = set()
seen.add(0)
for row in f.readlines():
    x = int(row)
    all_vals.append(x)
done = False
while not done:
    for i in all_vals:
        tot+=i
        if tot in seen:
            done=True
            break
        seen.add(tot)
print(tot)
