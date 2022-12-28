import numpy as np

input_file = 'day09_input.txt'

# read all input
with open(input_file) as f:
    input_data = f.read()

input_parts = input_data.split("\n")

def fsign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

class  Point:
    def __init__(self,x,y):
        self.x=int(x)
        self.y=int(y)
    def set(self,x,y):
        self.x=x
        self.y=y
    def get(self):
        return self.x, self.y
    def move(self,direction,steps):
        if direction == 'R':
            self.x=self.x + steps
        elif direction == 'L':
            self.x=self.x - steps
        elif direction == 'U':
            self.y = self.y - steps
        elif direction == 'D':
            self.y = self.y + steps
        else:
            print('Wrong direction ',direction)
            exit
    def catchup(self, head, board , markpoint = True):
        #print(head.x,head.y)
        # if distance is more than 1 move tail
        moved=False
        if abs(self.x - head.x) >1 or abs(self.y - head.y) > 1:
            self.x = self.x + fsign(head.x-self.x)
            self.y = self.y + fsign(head.y-self.y)
            #print(self.x,self.y)
            if markpoint:
                board[self.x,self.y]=1
            moved=True
        return moved


width=1000
height=1000
board = np.zeros((width,height),dtype=int)

start = Point(width/2,height/2)
head = Point(width/2,height/2)
tail = Point(width/2,height/2)

board[tail.x,tail.y] = 1

for i in input_parts:
    movement = i.split(" ")
    head.move(movement[0],int(movement[1]))
    while tail.catchup(head,board):
        True
        #print(tail.x,tail.y)

visited=0
for y in range(0,height -1):
    for x in range(0,width - 1):
        visited += board[x,y]
        #print(board[x,y],end="")
    #print("")

print("tail visited ",visited," positions")

# part 2
# 10 knots
#new board with zeros
board = np.zeros((width,height),dtype=int)
#mark start position
board[int(width/2),int(height/2)]=1
#create rope of points
rope = np.ndarray((10),dtype=Point)
#set all knots to start in center
for i in range(0,10):
    rope[i]=Point(width/2,height/2)
for i in input_parts:
    movement = i.split(" ")
    for steps in range(0,int(movement[1])):
        # Move only one step to let the whole rope catch up fore every step
        rope[0].move(movement[0],1)
        for j in range(1,9):
            while rope[j].catchup(rope[j-1],board,False):
                True
                #print(tail.x,tail.y)
        while rope[9].catchup(rope[8],board,True):
            True

visited=0
for y in range(0,height -1):
    for x in range(0,width - 1):
        visited += board[x,y]

print("Tail of rope with ten knots visited ",visited," positions")

for y in range(200,505):
    for x in range(474,639):
        print(board[x,y],end="")
    print("")