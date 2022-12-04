def subsets(pair):
    if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
        return 1
    elif pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]:
        return 1
    else:
        return 0

def subsets2(pair):
    if pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1]:
        return 1
    elif pair[1][0] >= pair[0][0] and pair[1][0] <= pair[0][1]:
        return 1
    else:
        return 0

with open('input.txt', 'r') as infile:
    thefile = infile.read().splitlines()
    
    pairs = [[[int(z) for z in y.split("-")] for y in x.split(",")] for x in thefile]
    
    print(sum(subsets(x) for x in pairs))
    print(sum(subsets2(x) for x in pairs))
