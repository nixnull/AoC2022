with open('input.txt', 'r') as infile:
    elves = [[int(c) for c in x.split("\n")] for x in infile.read()[:-1].split("\n\n")]
    
    print(f"Part A, Top Elf: {max(sum(x) for x in elves)}")
    
    print(f"Part B, Top Three Elves Summed: {sum(sorted([sum(x) for x in elves])[-3:])}")
