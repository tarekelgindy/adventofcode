input_file = 'sample2.txt'
input_file = 'input.txt'
f = open(input_file,'r')
tot = 0
s = ''
for row in f.readlines():
    s+=row
s=s.strip()
stay = [0 for j in range(len(s))]
done=False
cnt = 0
while not done:
    i=0
    done=True
    while i<len(stay):
        if stay[i]==1:
            i+=1
            continue
        nxt = i+1
        while nxt<len(stay) and stay[nxt] == 1:
            nxt+=1
        adder=0
        if nxt>=len(stay):
            i=nxt+adder
            continue
        if row[i].lower() == row[nxt].lower() and row[i]!=row[nxt]:
            done=False
            stay[nxt]=1
            stay[i]=1
            adder=1
        i=nxt+adder
res=0
output = ''
for i in range(len(stay)):
    if stay[i]==0:
        output+=s[i]
        res+=1
print(len(output))
print(res)
for i in range(len(output)-1):
    if output[i].lower() == output[i+1].lower() and output[i]!=output[i+1]:
        print(i,output[i],output[i+1])
