input_file = 'sample2.txt'
input_file = 'input.txt'
f = open(input_file,'r')
s_orig = ''
for row in f.readlines():
    s_orig+=row
s_orig=s_orig.strip()
for c in range(26):
    done=False
    s = s_orig.replace(chr(ord('a')+c),'').replace(chr(ord('A')+c),'')
    stay = [0 for j in range(len(s))]
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
            if s[i].lower() == s[nxt].lower() and s[i]!=s[nxt]:
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
    print(res)
