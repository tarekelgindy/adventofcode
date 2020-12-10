def isint(s):
    try:
        int(s)
        return True
    except:
        return False

def is_height(s):
    if s.endswith('in') or s.endswith('cm'):
        ok = True
    else:
        return False
    if s.endswith('in') and len(s)==4 and isint(s[:2]) and int(s[:2])>=59 and int(s[:2])<=76:
        return True
    if s.endswith('cm') and len(s)==5 and isint(s[:3]) and int(s[:3])>=150 and int(s[:3])<=193:
        return True
    return False
def is_hex(s):
    ok = True
    if s[0]!='#':
        return False
    for i in s[1:]:
        if not i in ["0",'1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
            ok = False
    return ok

good = 0
good2 = 0
data = []
vals = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] #,'cid']
#for row in open('test3.txt'):
for row in open('input.txt'):
    data.append(row.strip())
reset=True
curr_set = set()
curr_set2 = set()
for element in data:
    if element.strip()=='':
        #print(curr_set2)
        if len(curr_set)==7:
            good+=1
        if len(curr_set2)==7:
            good2+=1
        curr_set = set()
        curr_set2 = set()
        continue
    tokens = element.split()
    for token in tokens:
        if token.split(':')[0] in vals:
            curr_set.add(token.split(':')[0])
        if token.split(':')[0] in vals:
            key = token.split(':')[0]
            value = token.split(':')[1]
            if key =='byr' and isint(value) and int(value) >=1920 and int(value) <=2002:
                #print(token)
                curr_set2.add(token.split(':')[0])
            if key =='iyr' and isint(value) and int(value) >=2010 and int(value) <=2020:
                #print(token)
                curr_set2.add(token.split(':')[0])
            if key =='eyr' and isint(value) and int(value) >=2020 and int(value) <=2030:
                #print(token)
                curr_set2.add(token.split(':')[0])
            if key =='ecl' and value in ['amb','blu','brn','gry','grn','hzl','oth']:
                #print(token)
                curr_set2.add(token.split(':')[0])
            if key =='pid' and isint(value) and len(value)==9:
                #print(token)
                curr_set2.add(token.split(':')[0])
            if key =='hcl' and len(value) ==7 and is_hex(value):
                #print(token)
                curr_set2.add(token.split(':')[0])
            if key =='hgt' and is_height(value):
                #print(token)
                curr_set2.add(token.split(':')[0])
if len(curr_set)==7:
    good+=1
if len(curr_set2)==7:
    good2+=1
print(good)
print(good2)
