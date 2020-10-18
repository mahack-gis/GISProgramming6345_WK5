#File must be saved in the same location as your .py file.
#Code below is to open file and prepare to read it. 'r' read , 'w' write.
# '\n' refers to the end of the line (escape character)
# -1 goes to the last letter but does not include it.
#strip method code automatically removes '\n'

file = open('testWords.txt', 'r')
f = file.readlines()

#print(f)

newList = []
for line in f:
    if line[-1] == '\n':
        newList.append(line[:-1])
        #   #newList.append(line.strip())
    else:
        newList.append(line)

print(newList)
