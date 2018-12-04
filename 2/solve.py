input_file = 'sample1.txt'
input_file = 'input.txt'
two_cnt = 0
three_cnt = 0
for row in open(input_file,'r').readlines():
    cnt = [0 for i in range(26)]
    for i in row:
        pos = ord(i)-ord('a')
        if pos<26 and pos>=0:
            cnt[pos]+=1
    has_two = False
    has_three = False
    for i in cnt:
        if i ==2:
            has_two=True
        if i==3:
            has_three = True
    if has_two:
        two_cnt+=1
    if has_three:
        three_cnt+=1

print(two_cnt,three_cnt,two_cnt*three_cnt)

