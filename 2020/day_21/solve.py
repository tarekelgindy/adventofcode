data = []
#for row in open('input.txt'):
for row in open('test.txt'):
    data.append(row.strip())
all_ingredients = []
all_ingredients_list = []
all_alergens = []
ingredient_set = set()
alergen_set = set()
for row in data:
    sp = row.split()
    is_ingredient = True
    ingredients= []
    alergens = []
    for token in sp:
        if token.startswith('('):
            is_ingredient = False
            continue
        if is_ingredient:
            ingredients.append(token)
            all_ingredients_list.append(token)
            ingredient_set.add(token)
        else:
            alergens.append(token[:-1])
            alergen_set.add(token[:-1])
    all_alergens.append(alergens)
    all_ingredients.append(ingredients)

good=set()
for i in ingredient_set:
    is_alergen =False
    for j in alergen_set:
        contradicts = False
        for k in range(len(all_ingredients)):
            if j in all_alergens[k] and not i in all_ingredients[k]:
                contradicts = True
                break
        if not contradicts:
            is_alergen=True
            break
    if not is_alergen:
        good.add(i)

print(good)


res = 0
bad = set()
for i in all_ingredients_list:
    if i in good:
        res+=1
    else:
        bad.add(i)
print(res)
res2={}
for i in bad:
    for j in alergen_set:
        assigned=True
        for k in range(len(all_ingredients)):
            if j in all_alergens[k] and not i in all_ingredients[k]:
                assigned=False
                break
        if assigned:
            if not i in res2:
                res2[i]=set()
            res2[i].add(j)

# Two approaches from here - get maxium matching
# OR iteratively remove elements
import networkx as nx
from networkx.algorithms import bipartite
g=nx.Graph()
edges = []
top_nodes = set()
bottom_nodes = set()
for i in res2:
    top_nodes.add(i)
    for j in res2[i]:
        bottom_nodes.add(j)
        edges.append((i,j))

top_nodes = list(top_nodes)
bottom_nodes = list(bottom_nodes)
g.add_nodes_from(top_nodes,bipartite=0)
g.add_nodes_from(bottom_nodes,bipartite=1)
g.add_edges_from(edges)
res3=bipartite.matching.hopcroft_karp_matching(g, top_nodes)

for i in bad:
    print(i,res3[i])

res2_final = {}
while len(res2) >0:
    to_remove = None
    value_to_remove=None
    for i in res2:
        if len(res2[i])==1:
            value_to_remove= res2[i].pop()
            to_remove = i
            res2_final[i] = value_to_remove
            break
    res2.pop(i)
    for i in res2:
        if value_to_remove in res2[i]:
            res2[i].remove(value_to_remove)
to_sort = []
for i in res2_final:
    to_sort.append((res2_final[i],i))
to_sort=sorted(to_sort)
output=''
for i in to_sort:
    output+=i[1]+','
output=output[:-1]
print(output)


