def count_brackets(row2, position, end):
    bracket_count = 1
    new_start = position
    new_end = end
    for i in range(position,end):
        if row2[i] == '(':
            bracket_count+=1
        if row2[i] == ')':
            bracket_count-=1
        if bracket_count == 0:
            new_end = i
            break
    return (new_start,new_end)

def count_backwards(row2,position,start):
    bracket_count = 0
    new_start = start
    new_end = position
    for i in range(position-1,start,-1):
        if row2[i] == '(':
            bracket_count+=1
        if row2[i] == ')':
            bracket_count-=1
        if bracket_count == 0:
            new_start = i
            break
    return (new_start,new_end) 
        


def insert_brackets(row2):
    result = row2
    position = 0
    while position < len(result):
        if result[position]=='+':
            if result[position-1] != ')':
                result = result[:position-1]+'('+result[position-1]+'+'+result[position+1:]
            else:
                new_start,new_end = count_backwards(result,position,0)
                print(new_start,new_end)
                result = result[:new_start]+'('+result[new_start:]
            position+=2
            if position < len(result)-1 and result[position] != '(':
                result = result[:position+1]+')'+result[position+1:]
                position+=2
            elif position < len(result)-1:
                new_start,new_end = count_brackets(result,position+1,len(result))
                result = result[:new_end]+')'+result[new_end:]
                position+=1
            else:
                result = result+')'
        else:
            position+=1

                
    return result


def evaluate(row2,start,end):
    if row2[start] =='(':
        result=0
        position = start 
    else:
        result = int(row2[start])
        position = start+1
    while position < end:
        #print(start,end,position)
        char = row2[position]
        if char == '+':
            if row2[position+1] !='(':
                result += int(row2[position+1])
                position+=2
            else:
                new_start,new_end = count_brackets(row2,position+2,end)
                result+=evaluate(row2,new_start,new_end)
                position = new_end+1

        if char == '*':
            if row2[position+1] !='(':
                result *= int(row2[position+1])
                position+=2
            else:
                new_start,new_end = count_brackets(row2,position+2,end)
                result*=evaluate(row2,new_start,new_end)
                position = new_end+1
        if char == '(':
            new_start,new_end = count_brackets(row2,position+1,end)
            result=evaluate(row2,new_start,new_end)
            position = new_end+1

    return result



data = []

#for row in open('test.txt'):
for row in open('input.txt'):
    data.append(row.strip())
part1=0
part2=0
for row in data:
    row2 = row.replace(' ','')
    part1+=evaluate(row2,0,len(row2))
    row2 = insert_brackets(row2)
    part2+=evaluate(row2,0,len(row2))
    print(row2)
print(part1)
print(part2)
    

