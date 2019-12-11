input_file = 'input.txt'
input_file = 'sample1.txt'
f = open(input_file,'r')
tot = 0
for row in f.readlines():
    x = int(row)
    tot+=x
print(tot)
