def stack_exchange(item,stack):
    return [item] + stack

with open('input.txt', 'r') as infile:
    thefile = infile.read().splitlines()
    thestacks = thefile[0:8]
    
    stacks = [[],[],[],[],[],[],[],[],[]]
    
    for i in thefile[0:8]:
        if i[1] != " ":
            stacks[0] += i[1]
        if i[5] != " ":
            stacks[1] += i[5]
        if i[9] != " ":
            stacks[2] += i[9]
        if i[13] != " ":
            stacks[3] += i[13]
        if i[17] != " ":
            stacks[4] += i[17]
        if i[21] != " ":
            stacks[5] += i[21]
        if i[25] != " ":
            stacks[6] += i[25]
        if i[29] != " ":
            stacks[7] += i[29]
        if i[33] != " ":
            stacks[8] += i[33]

    instructions = thefile[10:512]
    
    # for i in instructions:
    #     for j in range(int(i[5:7])):
    #         from_s = int(i[12:14])-1
    #         to_s = int(i[17:19])-1
    #         stacks[to_s] = [stacks[from_s][0]] + stacks[to_s]
    #         stacks[from_s] = stacks[from_s][1:]
    for i in instructions:
            number = int(i[5:7])
            from_s = int(i[12:14])-1
            to_s = int(i[17:19])-1
            stacks[to_s] = stacks[from_s][0:number] + stacks[to_s]
            stacks[from_s] = stacks[from_s][number:]
            
    for stack in stacks:
        print(stack[0])
    print([x[0] for x in stacks)

