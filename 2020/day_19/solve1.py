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
        #print(value,all_res)
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
#for row in open('test.txt'):
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
#print(result)
total = 0
for row in data:
    if row.startswith('a') or row.startswith('b'):
        if row in result:
            print(row)
            total+=1
print(total)
        

