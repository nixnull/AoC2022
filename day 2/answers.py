rock, paper, scissors = 1, 2, 3

def playType(x):
    if x in ['A', 'X']:
        return rock
    elif x in ['B', 'Y']:
        return paper
    elif x in ['C', 'Z']:
        return scissors
    
def matchResult(x, y):
    if x == y:
        return 3 + y
    elif (x - y) in [1,-2]:
        return y
    else:
        return 6 + y
        
def response(x,y):
    if y == 'X': #Lose
        if x == 1:
            return 3
        return x-1
    if y == 'Y': #Draw
        return(x)
    if y == 'Z': #Win
        if x == 3:
            return 1
        return x+1

with open('input.txt', 'r') as infile:    
    print(f'Part A: {sum([matchResult(playType(lst[0]),playType(lst[2])) for lst in infile.read().splitlines()])}')
    
with open('input.txt', 'r') as infile:    
    print(f'Part B: {sum([matchResult(playType(lst[0]),response(playType(lst[0]),lst[2])) for lst in infile.read().splitlines()])}')
