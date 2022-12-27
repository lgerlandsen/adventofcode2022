import numpy as np

input_file = 'day08_input.txt'

# read all input
with open(input_file) as f:
    input_data = f.read()

input_parts = input_data.split("\n")

class Tree:
    def __init__(self,height):
        self.height = int(height)
        self.visible = False
        self.scenicscore = 0

    def check_visibility(self, maxheight):
        self.visible = self.visible or maxheight < self.height
        return self.visible


x=len(input_parts[0])
y=len(input_parts)

print('x=',x,' y=',y)

forest = np.ndarray((x,y),dtype=Tree)
y=0
for i in input_parts:
    x=0
    for j in list(i):
        #print(j, end="")
        forest[x,y] = Tree(j)
        #print(forest[x,y].height, end="")
        x += 1
    #print("")
    y += 1

print(forest.size)

print( forest.ndim )
print( forest.shape)

xsize=forest.shape[0] 
ysize=forest.shape[1] 


def print_visible_trees():
    print('** FOREST **')
    for y in range(0,ysize):
        for x in range(0,xsize):
            if forest[x,y].visible:
                print('T',end="")
            else:
                print('.',end="")
        print("")

# Four double loops to check all directions
for y in range(0,ysize):
    #print(y,':',end="")
    # maxsize = -1 to make sure edge is visible
    maxsize = -1
    for x in range(0,xsize):
        #print(forest[x,y].height, end="")
        if forest[x,y].check_visibility(maxsize):
            if maxsize < forest[x,y].height:
                maxsize = forest[x,y].height

#print_visible_trees()

for y in range(0,ysize):
    #print(y,':',end="")
    # maxsize = -1 to make sure edge is visible
    maxsize = -1
    for x in range(xsize-1,-1,-1):
        #print(forest[x,y].height, end="")
        if forest[x,y].check_visibility(maxsize):
            if maxsize < forest[x,y].height:
                maxsize = forest[x,y].height

#print_visible_trees()

for x in range(0,xsize):
    #print(x,':',end="")
    # maxsize = -1 to make sure edge is visible
    maxsize = -1
    for y in range(0,ysize):
        if forest[x,y].check_visibility(maxsize):
            if maxsize < forest[x,y].height:
                maxsize = forest[x,y].height

#print_visible_trees()

for x in range(0,xsize):
    #print(x,':',end="")
    # maxsize = -1 to make sure edge is visible
    maxsize = -1
    for y in range(ysize-1,-1,-1):
        #print(forest[x,y].height, end="")
        if forest[x,y].check_visibility(maxsize):
            if maxsize < forest[x,y].height:
                maxsize = forest[x,y].height

#print_visible_trees()

visible_trees = 0
for y in range(0,ysize):
    maxsize = -1
    for x in range(0,xsize):
        if forest[x,y].visible:
            visible_trees += 1
        
print("Visible trees: ", visible_trees)

#  part 2

def find_scenic_score(x,y):
    h = forest[x,y].height
    # look up
    visible_up=0
    i=y-1
    while i >= 0:
        if forest[x,i].height < h:
            visible_up += 1
            i -= 1
        elif forest[x,i].height >= h:
            visible_up += 1
            break
        else:
            break
    # look down
    visible_down=0
    i=y+1
    while i < ysize:
        if forest[x,i].height < h:
            visible_down += 1
            i += 1
        elif forest[x,i].height >= h:
            visible_down += 1
            break
        else:
            break
    # look left
    visible_left=0
    i=x-1
    while i >= 0:
        if forest[i,y].height < h:
            visible_left += 1
            i -= 1
        elif forest[i,y].height >= h:
            visible_left += 1
            break
        else:
            break
    # look right
    visible_right=0
    i=x+1
    while i < xsize:
        if forest[i,y].height < h:
            visible_right += 1
            i += 1
        elif forest[i,y].height >= h:
            visible_right += 1
            break
        else:
            break
    return visible_up * visible_down * visible_right * visible_left

    

maxscore = 0
treescore = 0
for y in range(0,ysize):
    maxsize = -1
    for x in range(0,xsize):
        print(forest[x,y].height,end="")
        treescore = find_scenic_score(x,y)
        if treescore > maxscore:
            maxscore=treescore
        print('(',treescore,')',end="")
        forest[x,y].scenicscore = treescore
    print("")

print('Max scenic score: ', maxscore)
