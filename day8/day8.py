import numpy as np
from numpy.core.numeric import zeros_like

def containsAll(str, set):
    """ Check whether sequence str contains ALL of the items in set. """
    return 0 not in [c in str for c in set]
def containsAny(str, set):
    """ Check whether sequence str contains ANY of the items in set. """
    return 1 in [c in str for c in set]

f = open("C:\\Users\\rick\\Desktop\\advent\\day8\\input.bib", "r")
# f = open("C:\\Users\\rick\\Desktop\\advent\\day8\\test", "r")
Lines = f.readlines()
f.close()

Lines = [Lines[x].split(" | ") for x in range(len(Lines))]


input = [Lines[x][0] for x in range(0, len(Lines))]
output = [Lines[x][1] for x in range(0, len(Lines))]

output_d = [output[x].replace("\n", "").split(" ") for x in range(len(output))]

res = [0, 0, 0, 0]
# [1, 4, 7, 8]
for i in range(len(output_d)):
    for j in range(len(output_d[0])):
        if len(output_d[i][j])== 2:
            res[0]+=1
        elif len(output_d[i][j])== 4:
            res[1]+=1
        elif len(output_d[i][j])== 3:
            res[2]+=1
        elif len(output_d[i][j])== 7:
            res[3]+=1
arr = np.asarray(res)
print(arr.sum())


# ---------------------------------

input_d = [input[x].replace("\n", "").split(" ") for x in range(len(input))]

decoding = np.empty_like(input_d)

leds = []
for i in range(len(input_d)):
    leds_row = ["", "", "", "", "", "", "", "", "", ""]
    for j in range(len(input_d[0])):
        if len(input_d[i][j])== 2:
            decoding[i][j] = 1
            leds_row[1] = ''.join(sorted(input_d[i][j]))
        elif len(input_d[i][j])== 4:
            decoding[i][j] = 4
            leds_row[4] = ''.join(sorted(input_d[i][j]))
        elif len(input_d[i][j])== 3:
            decoding[i][j] = 7
            leds_row[7] = ''.join(sorted(input_d[i][j]))
        elif len(input_d[i][j])== 7:
            decoding[i][j] = 8
            leds_row[8] = ''.join(sorted(input_d[i][j]))
    leds.append(leds_row)


# for i in range(len(input_d)):
#     for j in range(len(input_d[0])):
#         if len(input_d[i][j])== 5:
#             if ''.join(sorted(input_d[i][j])).find(leds[i][1]):
#                 decoding[i][j] = 3
#                 leds[i][3] = ''.join(sorted(input_d[i][j]))
#             elif (not (''.join(sorted(input_d[i][j])).find(leds[i][1])) ) and ((not (''.join(sorted(input_d[i][j])).find(leds[i][4])) )) and ((not (''.join(sorted(input_d[i][j])).find(leds[i][7])) )):
#                 decoding[i][j] = 5
#                 leds[i][5] = ''.join(sorted(input_d[i][j]))
#             else:
#                 decoding[i][j] = 2
#                 leds[i][2] = ''.join(sorted(input_d[i][j]))
#         elif len(input_d[i][j])== 6:
#             if  (not (''.join(sorted(input_d[i][j])).find(leds[i][1])) ):
#                 decoding[i][j] = 0
#                 leds[i][0] = ''.join(sorted(input_d[i][j]))
#             elif (''.join(sorted(input_d[i][j])).find(leds[i][1])) and (''.join(sorted(input_d[i][j])).find(leds[i][4])) and (''.join(sorted(input_d[i][j])).find(leds[i][7])) :
#                 decoding[i][j] = 9
#                 leds[i][9] = ''.join(sorted(input_d[i][j]))
#             else:
#                 decoding[i][j] = 6
#                 leds[i][6] = ''.join(sorted(input_d[i][j]))

for i in range(len(input_d)):
    for j in range(len(input_d[0])):
        if len(input_d[i][j])== 5:
            if (containsAll(input_d[i][j], leds[i][1])):
                decoding[i][j] = 3
                leds[i][3] = ''.join(sorted(input_d[i][j]))
            elif containsAll(input_d[i][j]+leds[i][4], leds[i][8]) :
                decoding[i][j] = 2
                leds[i][2] = ''.join(sorted(input_d[i][j]))
            else:
                decoding[i][j] = 5
                leds[i][5] = ''.join(sorted(input_d[i][j]))
        elif len(input_d[i][j])== 6:
            if  (not (containsAll(input_d[i][j], leds[i][1]))) and (not(containsAll(input_d[i][j], leds[i][4]))) and (not (containsAll(input_d[i][j], leds[i][7]))):
                decoding[i][j] = 6
                leds[i][6] = ''.join(sorted(input_d[i][j]))
            elif (containsAll(input_d[i][j], leds[i][1])) and (containsAll(input_d[i][j], leds[i][4])) and (containsAll(input_d[i][j], leds[i][7])) :
                decoding[i][j] = 9
                leds[i][9] = ''.join(sorted(input_d[i][j]))
            else:
                decoding[i][j] = 0
                leds[i][0] = ''.join(sorted(input_d[i][j]))



decoding_out = np.empty_like(output_d)
for i in range(len(output_d)):
    for j in range(len(output_d[0])):
        if ''.join(sorted(output_d[i][j]))==  leds[i][0]:
            decoding_out[i][j] = 0
        elif ''.join(sorted(output_d[i][j]))==  leds[i][1]:
            decoding_out[i][j] = 1
        elif ''.join(sorted(output_d[i][j]))==  leds[i][2]:
            decoding_out[i][j] = 2
        elif ''.join(sorted(output_d[i][j]))==  leds[i][3]:
            decoding_out[i][j] = 3
        elif ''.join(sorted(output_d[i][j]))== leds[i][4]:
            decoding_out[i][j] = 4
        elif ''.join(sorted(output_d[i][j]))== leds[i][5]:
            decoding_out[i][j] = 5
        elif ''.join(sorted(output_d[i][j]))==  leds[i][6]:
            decoding_out[i][j] = 6
        elif ''.join(sorted(output_d[i][j]))==  leds[i][7]:
            decoding_out[i][j] = 7
        elif ''.join(sorted(output_d[i][j]))==  leds[i][8]:
            decoding_out[i][j] = 8
        elif ''.join(sorted(output_d[i][j]))==  leds[i][9]:
            decoding_out[i][j] = 9

numbers = np.zeros(len(output_d))
for i in range(len(output_d)):
    numbers[i] = int(str(decoding_out[i]).replace("[", "").replace("]", "").replace("'", "").replace(" ", ""))

print(numbers.sum())
