good = 0
good2 = 0
for row in open('input.txt'):
    data = row.split()
    nums = data[0].split('-')
    low = int(nums[0])
    high = int(nums[1])
    let = data[1][0]
    s = data[2]
    cnt = 0
    cnt2 = 0
    for i in s:
        if i==let:
            cnt+=1
    if cnt <=high and cnt >=low:
        good+=1
    if s[low-1] ==let:
        cnt2+=1
    if s[high-1] ==let:
        cnt2+=1
    if cnt2 == 1:
        good2+=1
print(good)
print(good2)
