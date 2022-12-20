import copy

input_file = 'day05_input.txt'

# read all input
with open(input_file) as f:
    input_data = f.read()

input_parts = input_data.split("\n\n")

move_instructions = input_parts[1].split("\n")

# split into strings
shipment = input_parts[0].split("\n")
# create array of characters
for i in shipment:
    i = list(i)

stacks = []

firstrow = True
i=len(shipment)
while i > 0:
    i -= 1
    j = 0
    k = 0
    while j < len(shipment[i]):
        if (j+3) % 4 == 0: 
            #print(shipment[i][j], end="")
            if firstrow:
                stacks.append([shipment[i][j]])
            elif shipment[i][j] != " ":
                stacks[k].append(shipment[i][j])
            k += 1
        j += 1
    firstrow = False
    #print()

stacks_part2 = []
stacks_part2 = copy.deepcopy(stacks)

def print_stacks(thestacks):
    for i in thestacks:
        print(i)

def move_one(fromstack, tostack):
    fromstack -= 1
    tostack -= 1
    stacks[tostack].append(stacks[fromstack][-1])
    del stacks[fromstack][-1]

print_stacks(stacks) 


for i in move_instructions:
    move_instructions[move_instructions.index(i)] = i.split(" ")

for i in move_instructions:
    number = int(i[1])
    fromstack = int(i[3])
    tostack = int(i[5])
    while number > 0:
        move_one(fromstack, tostack)
        number -= 1

print_stacks(stacks)

print('Top crates: ', end="")
for i in stacks:
    print(i[-1], end="")
print()


def move_multiple(number,fromstack,tostack):
    fromstack -= 1
    tostack -= 1
    while number > 0:
        stacks_part2[tostack].append(stacks_part2[fromstack][-number])
        del stacks_part2[fromstack][-number]
        number -= 1

#move_multiple(2,1,2)
#print_stacks(stacks_part2)

for i in move_instructions:
    number = int(i[1])
    fromstack = int(i[3])
    tostack = int(i[5])
    move_multiple(number,fromstack,tostack)

print_stacks(stacks_part2)
print('Top crates part 2: ', end="")
for i in stacks_part2:
    print(i[-1], end="")
print()
