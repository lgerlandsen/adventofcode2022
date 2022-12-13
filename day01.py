input_file = 'day01_input.txt'

# read all input
with open(input_file) as f:
    input_data = f.read()

# split it on each elf
a_elves = input_data.split("\n\n")

# create Knapsack object for each elf
class  Knapsack:
    def __init__ (self,elf_number, a_content ):
        self.number = elf_number
        self.a_content = [int(i) for i in a_content.split("\n")]
        self.calories = sum(self.a_content)


# Give all elves a Knapsack to carry stuff
for i in a_elves:
    a_elves[a_elves.index(i)] = Knapsack(a_elves.index(i),i)

elf_carrying_most=-1
elf_carrying_calories=-1
for i in a_elves:
    if i.calories > elf_carrying_calories:
        elf_carrying_most = a_elves.index(i)
        elf_carrying_calories = i.calories

print('Elf number ', elf_carrying_most + 1, ' carries ', elf_carrying_calories , 'calories')

# sort the array containing objects
a_elves_sorted = sorted(a_elves, key=lambda Knapsack: Knapsack.calories, reverse=True)
sum_calories=0
print("Top three:")
for i in [0,1,2]:
    sum_calories+=a_elves_sorted[i].calories
    print('Elf number:',a_elves_sorted[i].number + 1, ' carries ', a_elves_sorted[i].calories , ' calories')

print('Total for top three ', sum_calories, ' calories')
