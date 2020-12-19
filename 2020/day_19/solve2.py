def eight_inside(curr_str,eightset):
    all_eights = set([curr_str]) 
    for e in eightset:
        if curr_str.startswith(e):
            remainder = eight_inside(curr_str[len(e):],eightset)
            all_eights = all_eights.union(remainder)
    return all_eights

def eleven_inside(possible_strs,fortytwo_set,thirtyone_set):
    possible = False
    for sample1 in fortytwo_set:
        break
    for sample2 in thirtyone_set:
        break
    for s in possible_strs:
        if len(s) == 0:
            return True
        if len(s)%(len(sample1)+len(sample2) ) !=0:
            continue
        all_reduced = set()
        for i in fortytwo_set:
            for j in thirtyone_set:
                if s.startswith(i) and s.endswith(j):
                    reduced = s[len(i):-1*len(j)]
                    all_reduced.add(reduced)
        if len(all_reduced)>0:
            result = eleven_inside(all_reduced,fortytwo_set,thirtyone_set)
            if result:
                return True
    return False


seen = {}
def add_rules(value,rules,all_rules):
    if value in seen:
        return seen[value]
    res = ''
    if rules[0][0] =='a' or rules[0][0]=='b':
        return [rules[0][0]]
    all_results = []
    for option in rules:
        all_res = []
        for rule in option:
            all_returns = add_rules(rule,all_rules[rule],all_rules)
            all_res.append(all_returns)
        all_strings = all_res[0]
        if len(all_res)>1:
            for subset in all_res[1:]:
                combination = []
                for s in all_strings:
                    for nxt in subset:
                        combination.append(s+nxt)
                all_strings = combination
        all_results.extend(all_strings)


    seen[value] = all_results
    return all_results
data = []
#for row in open('test2.txt'):
for row in open('input.txt'):
    data.append(row.strip())

rules = {}
for row in data:
    if ':' in row:
        sp = row.split(':')
        name = sp[0]
        rule_list = []
        for rr in sp[1].split('|'):
            subrule = []
            for lookup in rr.strip().split():
                subrule.append(lookup.replace('"',''))
            rule_list.append(subrule)
        rules[name] = rule_list

result = set(add_rules('0',rules['0'],rules))
total = 0
part2 = []
for row in data:
    if row.startswith('a') or row.startswith('b'):
        if row in result:
            total+=1
        else:
            part2.append(row)
print(total)

extra = 0
for i in part2:
    prefixes = eight_inside(i,seen['8'])
    if '' in prefixes:
        prefixes.remove('')
    if i in prefixes:
        prefixes.remove(i)
    suffix = eleven_inside(prefixes,seen['42'],seen['31'])
    if suffix:
        extra+=1
print(extra+total)
