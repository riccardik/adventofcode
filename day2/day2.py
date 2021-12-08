f = open("C:\\Users\\rick\\Desktop\\advent\\day2\\input.bib", "r")
Lines = f.readlines()
f.close()

horiz = 0
depth = 0

for i in range(len(Lines)):
    line = Lines[i].split()
    if line[0] == 'forward':
        horiz += int(line[1])
    elif line[0] == 'down':
        depth += int(line[1])
    elif line[0] == 'up':
        depth -= int(line[1])

print(depth*horiz)



horiz = 0
depth = 0
aim = 0

for i in range(len(Lines)):
    line = Lines[i].split()
    if line[0] == 'forward':
        horiz += int(line[1])
        depth = depth+int(line[1])*aim
    elif line[0] == 'down':
        aim += int(line[1])
    elif line[0] == 'up':
        aim -= int(line[1])

print(depth*horiz)