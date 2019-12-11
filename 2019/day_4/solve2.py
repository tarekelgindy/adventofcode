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
        if ii[c] < ii[c-1]:
            increasing = False
    for j in range(10):
        mx = 0
        st = 0
        on = False
        for c in range(len(ii)):
            if ii[c] == str(j) and not on:
                on = True
            if ii[c] == str(j) and on:
                st+=1
            if ii[c] !=str(j):
                on = False
                if st > mx:
                    mx = st
        if on and st>mx:
            mx = st

        #print(j,mx)
        if mx == 2:
            pair = True

    if increasing and pair:
        cnt+=1
        print(ii)

print(cnt)
