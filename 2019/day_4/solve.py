input = '240298-784956'
sp = input.split('-')

cnt = 0
start = int(sp[0])
end = int(sp[1])
for i in range(start,end+1):
    ii = str(i)
    pair = False
    increasing = True
    for c in range(1,len(ii)):
        if ii[c] == ii[c-1]:
            pair = True
        if ii[c] < ii[c-1]:
            increasing = False
    if increasing and pair:
        cnt+=1
        print(ii)

print(cnt)
