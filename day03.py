input_file = 'day03_input.txt'

# read all input
with open(input_file) as f:
    input_data = f.read()

class  Knapsack:
    def __init__ (self,elf_number, a_content ):
        self.number = elf_number
        self.a_content = [int(i) for i in a_content.split("\n")]
        self.calories = sum(self.a_content)