input_file = 'day07_input.txt'

# read all input
with open(input_file) as f:
    input_data = f.read()

input_parts = input_data.split("\n")

class a_file:
    def __init__(self,name,size):
        self.name=name
        self.size=size

class directory:
    def __init__ (self,name,parent = None):
        self.name = name
        self.subdirs=[]
        self.files=[]
        self.directorysize=0
        self.parent=parent
        self.atmost = 0
        #if self.name != '/':
        #    print('Parent: ',self.parent.name, 'subdir: ',self.name)
    
    def add_subdir(self, name):
        self.subdirs.append(directory(name,self))

    def add_file(self,filename,size):
        self.files.append(a_file(filename,size))
        self.directorysize += size

    def finddir(self, dirname):
        for i in self.subdirs:
            if i.name == dirname:
                return i
    
    def totaldirectorysize(self, level):
        self.atmost = 0
        totalsize = self.directorysize
        for i in self.subdirs:
            a, b = i.totaldirectorysize(level + 1)
            totalsize += a
            self.atmost += b
        if totalsize <= 100000:
            self.atmost += totalsize
        #print('  '*level, 'Directory ', self.name, ' is ', totalsize, ' large. Size small directories: ', self.atmost)
        self.directorysize = totalsize
        return totalsize, self.atmost
                
    def dirtodelete(self, deletecandidate, deleteatleast ):
        totalsize = self.directorysize
        if totalsize >= deleteatleast and deletecandidate.directorysize > totalsize:
            deletecandidate = self
        for i in self.subdirs:
            deletecandidate = i.dirtodelete(deletecandidate, deleteatleast)
        return deletecandidate

rootdir = directory("/")

position = rootdir

lineno = 0
while lineno <  len(input_parts):
    i = input_parts[lineno].split(' ')
    if i[0] == '$':
        if i[1] == 'cd':
            if i[2] == '/':
                position=rootdir
            elif i[2] == '..':
                position=position.parent
            else:
                position=position.finddir(i[2])
            lineno += 1
        elif i[1] == 'ls':
            lineno += 1
            j = input_parts[lineno].split(' ')
            while j[0] != '$':
                if j[0] == 'dir':
                    position.add_subdir(j[1])
                else:
                    position.add_file(j[1],int(j[0]))
                lineno += 1
                if lineno >= len(input_parts):
                    break
                j = input_parts[lineno].split(' ')
                
while position.name != '/':
    position=position.parent

totalsize, atmost = position.totaldirectorysize(0)
print('Total size: ', totalsize)
print('At most 100000: ', atmost)

totaldisk = 70000000
spaceneeded = 30000000
freespace = totaldisk - totalsize
deleteatleast = spaceneeded - freespace
print('Need to delete at least ',deleteatleast)

dirtodelete = rootdir.dirtodelete(rootdir,deleteatleast)

print('Directory ', dirtodelete.name, ' Size: ',dirtodelete.directorysize)
#Total size:  46090134
#At most 100000:  1491614
#Need to delete at least  6090134
#Directory  qzgsswr  Size:  6400111
