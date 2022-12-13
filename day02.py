input_file = 'day02_input.txt'

# read all input
with open(input_file) as f:
    input_data = f.read()

a_guide = input_data.split("\n")

total_points=0
for i in a_guide:
    if   i.find('X')>0: total_points+=1
    elif i.find('Y')>0: total_points+=2
    elif i.find('Z')>0: total_points+=3
    else:
        print('Something not correct with input data *',i,'*')
        exit()
    # A rock
    # B paper
    # C scissors
    # X rock
    # Y paper
    # Z scissors
    if   i == 'A X': total_points+=3 
    elif i == 'A Y': total_points+=6
    elif i == 'A Z': total_points+=0
    elif i == 'B X': total_points+=0
    elif i == 'B Y': total_points+=3
    elif i == 'B Z': total_points+=6
    elif i == 'C X': total_points+=6
    elif i == 'C Y': total_points+=0
    elif i == 'C Z': total_points+=3
    else:
        print('Something wrong with input data *',i,'*')
        exit()

print('Total points ',total_points)

# A rock
# B paper
# C scissors
# X means you need to lose, 
# Y means you need to end the round in a draw, and 
# Z means you need to win.
total_points=0
for i in a_guide:
    if   i == 'A X': total_points+=3+0
    elif i == 'A Y': total_points+=1+3
    elif i == 'A Z': total_points+=2+6
    elif i == 'B X': total_points+=1+0
    elif i == 'B Y': total_points+=2+3
    elif i == 'B Z': total_points+=3+6
    elif i == 'C X': total_points+=2+0
    elif i == 'C Y': total_points+=3+3
    elif i == 'C Z': total_points+=1+6

print('Total point part 2:',total_points)
