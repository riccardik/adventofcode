import numpy as np

# f = open("C:\\Users\\rick\\Desktop\\advent\\day5\\input.bib", "r")
f = open("C:\\Users\\rick\\Desktop\\advent\\day5\\test", "r")
Lines = f.readlines()
f.close()

Lines = [Lines[x].split(" -> ") for x in range(len(Lines))]
inp = [Lines[x][0] for x in range(0, len(Lines))]
outp = [Lines[x][1] for x in range(0, len(Lines))]

inp = [inp[x].split(",") for x in range(len(inp))]
outp = [outp[x].replace("\n", "").split(",") for x in range(len(outp))]

inp = [[int(inp[x][0]),int(inp[x][1])]  for x in range(len(inp))]
outp = [[int(outp[x][0]),int(outp[x][1])]  for x in range(len(outp))]

size = [ max([max(outp[0]), max(inp[0])])+1 , max([max(outp[1]), max(inp[1])]) +1]

diagram = np.zeros([1000, 1000])

for i in range(len(inp)):
    if inp[i][0] == outp[i][0]:
        if inp[i][1]> outp[i][1]:
            coords = list(range(outp[i][1], inp[i][1]+1))
            for j in range(len(coords)):
                diagram [inp[i][0], coords[j]] +=1                
        elif inp[i][1]< outp[i][1]:
            coords = list(range(inp[i][1], outp[i][1]+1))
            for j in range(len(coords)):
                diagram [outp[i][0], coords[j]] +=1
    elif inp[i][1] == outp[i][1]:
        if inp[i][0]> outp[i][0]:
            coords = list(range(outp[i][0], inp[i][0]+1))
            for j in range(len(coords)):
                diagram [coords[j], inp[i][1] ] +=1
        elif inp[i][0]< outp[i][0]:
            coords = list(range(inp[i][0], outp[i][0]+1))
            for j in range(len(coords)):
                diagram[coords[j], outp[i][1]] +=1

diagram = diagram.transpose()

overlap = 0
for i in range(diagram.shape[0]):
    for j in range(diagram.shape[1]):
        if diagram[i, j]>1:
            overlap+=1
print( overlap)

# ---------------------------


diagram = np.zeros([1000, 1000])

for i in range(len(inp)):
    if inp[i][0] == outp[i][0]:
        if inp[i][1]> outp[i][1]:
            coords = list(range(outp[i][1], inp[i][1]+1))
            for j in range(len(coords)):
                diagram [inp[i][0], coords[j]] +=1                
        elif inp[i][1]< outp[i][1]:
            coords = list(range(inp[i][1], outp[i][1]+1))
            for j in range(len(coords)):
                diagram [outp[i][0], coords[j]] +=1
    elif inp[i][1] == outp[i][1]:
        if inp[i][0]> outp[i][0]:
            coords = list(range(outp[i][0], inp[i][0]+1))
            for j in range(len(coords)):
                diagram [coords[j], inp[i][1] ] +=1
        elif inp[i][0]< outp[i][0]:
            coords = list(range(inp[i][0], outp[i][0]+1))
            for j in range(len(coords)):
                diagram[coords[j], outp[i][1]] +=1
    elif inp[i][0] < outp[i][0]:
        if inp[i][1] < outp[i][1]:
            coords = list(range(inp[i][1], outp[i][1]+1))
            for j in range(len(coords)):
                diagram[inp[i][0]+j, inp[i][1]+j] +=1
        elif inp[i][1] > outp[i][1]:
            coords = list(range(outp[i][1], inp[i][1]+1))
            for j in range(len(coords)):
                diagram[inp[i][0]+j, inp[i][1]-j] +=1
    elif inp[i][0] > outp[i][0]:
        if inp[i][1] < outp[i][1]:
            coords = list(range(inp[i][1], outp[i][1]+1))
            for j in range(len(coords)):  
                diagram[inp[i][0]-j, inp[i][1]+j] +=1
        elif inp[i][1] > outp[i][1]:
            coords = list(range(outp[i][1], inp[i][1]+1))
            for j in range(len(coords)):
                diagram[inp[i][0]-j, inp[i][1]-j] +=1
    # print(diagram.transpose())
    # input()


diagram = diagram.transpose()

overlap = 0
for i in range(diagram.shape[0]):
    for j in range(diagram.shape[1]):
        if diagram[i, j]>1:
            overlap+=1
print(overlap)
