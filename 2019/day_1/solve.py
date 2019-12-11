tot = 0
tot2 = 0
for row in open('input.txt').readlines():
 val = int(row)
 res = int(val/3) -2 
 res2 = res
 final_res = res
 tot+=res
 while res2 >0:
  res2 = max(0,int(res2/3)-2)
  final_res += res2
 tot2 += final_res
 #print(final_res)
  
print(tot)
print(tot2)