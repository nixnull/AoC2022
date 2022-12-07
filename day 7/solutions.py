class directory:
        def __init__(self, name, parent=None):
            self.name = name
            self.parent = parent
            self.children = {}
            self.files = []
        
        def add_child(self, child):
            self.children[child.name] = child
            
        def add_file(self, f):
            self.files.append(f)
        
        def dir_size(self):
            return sum(self.files) + sum(self.children[x].dir_size() for x in self.children.keys())

with open('input.tx', 'r') as infile:
    thefile = infile.read().splitlines()

    directories = []
    root = directory("/")
    directories.append(root)
    current_dir = root
    
    for i in range(len(thefile)):
        if thefile[i][0:4] == "$ cd":
            if thefile[i][5:] == "/":
                current_dir = root
            elif thefile[i][5:] == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.children[thefile[i][5:]]
        elif thefile[i][0:4] == "$ ls":
            full_list = False
            lines = 0
            while not full_list and (len(thefile) > (i+lines+1)):
                lines+=1
                if thefile[i+lines][0:3] != "$ c":
                    if thefile[i+lines][0:3] == "dir":
                        nd = directory(thefile[i+lines][4:], current_dir)
                        directories.append(nd)
                        current_dir.add_child(nd)
                    else:
                        current_dir.add_file(int(thefile[i+lines].split(" ")[0]))
                else:
                    full_list = True
    
    total = 0
    free_needed = 30000000 - (70000000 - root.dir_size())
    
    total = sum(size for size in [dr.dir_size() for dr in directories] if size < 100000)
    
    deletion_size = min(size for size in [dr.dir_size() for dr in directories] if size >= free_needed)
    
    print(total)
    print(deletion_size)
