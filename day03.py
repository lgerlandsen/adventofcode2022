input_file = 'day03_input.txt'

# read all input
with open(input_file) as f:
    input_data = f.read()

a_input_data = input_data.split("\n")

            
def find_priority(item: str) -> int:
    priority = 0
    if (ord(item) < ord('a')):
        priority = ord(item) - ord('A') + 27
    else:
        priority = ord(item) - ord('a') + 1
    return priority 

class  Rucksack:
    def __init__ (self,elf_number, s_content ):
        self.number = elf_number
        self.content = s_content
        self.compartment1 = s_content[:int(len(s_content)/2)]
        self.compartment2 = s_content[ int(- len(s_content)/2):]

    def duplicate(self):
        itemvalue = 0
        for i in self.compartment1:
            for j in self.compartment2:
                if i == j: itemvalue=i
        return itemvalue


for i in a_input_data:
    a_input_data[a_input_data.index(i)] = Rucksack(a_input_data.index(i),  i )
    
i_sum_priorities = 0
for i in a_input_data:
    c_duplicate = i.duplicate()
    i_priority = find_priority(c_duplicate)
    i_sum_priorities += i_priority
    #print(i.number,'-',i.compartment1,'-',i.compartment2,'-',c_duplicate,'-',i_priority,'-',i_sum_priorities)
 
print('Sum of the priorities is ', i_sum_priorities)

group_priorities = 0
for i in range(0 , int(len(a_input_data)/3) ):
    itemvalue = 0
    group = i*3
    for j in a_input_data[group].content:
        for k in a_input_data[group+1].content:
            if j == k :
                for l in a_input_data[group+2].content:
                    if k == l:
                        itemvalue = l                     
    #print('Group number ',i+1, ' has item ',itemvalue,' in common')
    #print('Priority', find_priority(itemvalue))
    group_priorities+=find_priority(itemvalue)

print('Sum of group priorities is ',group_priorities)
