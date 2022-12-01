with open('input.txt', 'r') as infile:
    elves = [[int(c) for c in x.split("\n")] for x in infile.read()[:-1].split("\n\n")]
    
    print("Part A, Top Elf:")
    print(max(sum(x) for x in elves))
    
    print()
    
    print("Part B, Top Three Elves Summed:")
    print(sum(sorted([sum(x) for x in elves])[-3:]))
