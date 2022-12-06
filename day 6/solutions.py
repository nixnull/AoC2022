with open('input.txt', 'r') as infile:
    thefile = infile.read().splitlines()

    thestring = thefile[0]
	
    def first_unique_string(length):
        for i in range(length,len(thestring)):
            sett = thestring[(i-length):i]
			
            if not [x for x in sett if sett.count(x)>1]:
                return i
            
    print(first_unique_string(4))
    print(first_unique_string(14))
