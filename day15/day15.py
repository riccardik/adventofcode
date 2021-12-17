import numpy as np


# f = open("C:\\Users\\rick\\Desktop\\advent\\day15\\input.bib", "r")
f = open("C:\\Users\\rick\\Desktop\\advent\\day15\\test", "r")
Lines = f.readlines()
f.close()

input_f = []
for i in range(len(Lines)):
    line = Lines[i].replace("\n", "")
    row = []
    for j in range(len(line)):
        row.append(int(line[j]))
    input_f.append(row)

cave = np.asarray(input_f)

cost = 0
x = 0
y = 0
while(y<cave.shape[1]):
        if cave[x+1][y]>=cave[x][y+1]:
            x+=1
        else:
            y+=1
        cost += cave[x][y]