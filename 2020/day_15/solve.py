last_spoken = {}
inputs = [3,1,2]
inputs = [0,3,6]
inputs=[0,6,1,7,2,19,20]
end_num = 11
end_num = 2020+1
end_num = 30000000+1
for i in range(len(inputs)):
    last_spoken[inputs[i]]=i+1
prev_curr = 0
curr =0
count = len(inputs)+1
while count !=end_num:
    if count %1000000==0:
        print(count,flush=True)
    prev_curr=curr
    if curr in last_spoken:
        curr_nxt = count-last_spoken[curr]
        last_spoken[curr] = count
        curr=curr_nxt
    else:
        last_spoken[curr] = count 
        curr=0
    count+=1
print(prev_curr)


