data = []
#for row in open('test.txt').readlines():
for row in open('input.txt').readlines():
    data.append(row.strip())

start_num = 1
subject_number = 7
public_key = 17807724
public_key = 17115212
public_key2 = 3667832
divider = 20201227
res1 = 0
for i in range(10000000):
    start_num *= subject_number
    start_num = start_num%divider
    if start_num == public_key:
        res1=i+1
        break
print(res1)
res2=1
for i in range(res1):
    res2*=public_key2
    res2=res2%divider
print(res2)


