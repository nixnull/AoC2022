with open('input.txt', 'r') as infile:
    elves = [x.split("\n") for x in infile.read()[:-1].split("\n\n")]
    
    to_nums = lambda x: [eval(y) for y in x]
    
    elves = [to_nums(x) for x in elves]
    
    print("Part A, Top Elf:")
    print(sorted(sum(x) for x in elves)[-1:])
    
    print()
    
    print("Part B, Top Three Elves Summed:")
    print(sum(sorted([sum(x) for x in elves])[-3:]))
