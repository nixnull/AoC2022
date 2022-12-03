priorities = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
priorities += [x.upper() for x in priorities]

def findValue(x):
    for i in range(0,52):
        if x == priorities[i]:
            return(i+1)

def ruckItem(x):
    n = len(x)//2
    
    ruck1 = x[0:n]
    ruck2 = x[n:]
    
    for item in ruck1:
        if item in ruck2:
            return item

def badgeItem(x,y,z):
    for item in x:
        if (item in y) and (item in z):
            return item

with open('input.txt', 'r') as infile:
    thefile = infile.read().splitlines()
                
    print(f'Part A, Rucksack Item Sums: {sum([findValue(ruckItem(x)) for x in thefile])}')
    
    print(f'Part B, Badge Item Sums: {sum([findValue(badgeItem(thefile[i],thefile[i+1],thefile[i+2])) for i in range(0,len(thefile),3)])}')
