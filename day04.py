input_file = 'day04_input.txt'

# read all input
with open(input_file) as f:
    input_data = f.read()

a_pairs = input_data.split("\n")

class  Assignmentpairs:
    def __init__ (self,pair_number, s_content ):
        self.number = pair_number
        self.a_pair = s_content.split(',')
        self.a_pair1 = self.a_pair[0].split('-')
        self.a_pair2 = self.a_pair[1].split('-')
        
    def one_contains(self, p1, p2):
        if int(p1[0]) >= int(p2[0]) and int(p1[1]) <= int(p2[1]):
            return True
        else:
            return False

    def overlap(self):
        if     int(self.a_pair1[0]) >= int(self.a_pair2[0]) and int(self.a_pair1[0]) <= int(self.a_pair2[1]) \
            or int(self.a_pair1[1]) >= int(self.a_pair2[0]) and int(self.a_pair1[1]) <= int(self.a_pair2[1]) \
            or int(self.a_pair2[0]) >= int(self.a_pair1[0]) and int(self.a_pair2[0]) <= int(self.a_pair1[1]) \
            or int(self.a_pair2[1]) >= int(self.a_pair1[0]) and int(self.a_pair2[1]) <= int(self.a_pair1[1]) :
            return True
        else:
            return False

    def contains(self):
        return self.one_contains(self.a_pair1,self.a_pair2) or self.one_contains(self.a_pair2,self.a_pair1)

for i in a_pairs:
    a_pairs[a_pairs.index(i)] = Assignmentpairs(a_pairs.index(i),  i )
    
count = 0
count_overlaps = 0
for i in a_pairs:
    if i.contains():
        count += 1
    if i.overlap():
        count_overlaps += 1     

print('Total number of contained pairs is ', count )
print('Total number of overlaps is ', count_overlaps)