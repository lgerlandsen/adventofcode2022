input_file = 'day06_input.txt'

# read all input
with open(input_file) as f:
    input_data = f.read()

characterstream = list(input_data)

c1=""
c2=""
c3=""
c4=""
marker_after = 0
count=0
for i in characterstream:
    c1=c2
    c2=c3
    c3=c4
    c4=i
    count += 1
    if c1!="" and c2!="" and c3!="":
        if not ( c1==c2 or c1==c3 or c1 == c4 or c2==c3 or c2==c4 or c3==c4 ):
            # found it 
            #print(c1,c2,c3,c4)
            marker_after = count
            break
print('Found marker after ', marker_after)

# part 2
count = 13
inputlength=len(input_data)
while count < inputlength:
    count += 1
    stringtotest=input_data[count-14:count]
    i=0
    foundsimilar = False
    while i < 13:
        j=i+1
        while j <= 13:
            if stringtotest[i] == stringtotest[j]:
                foundsimilar=True
            j += 1
        i += 1
    if not foundsimilar:
        print( count, ' : ' , stringtotest)
        break
    