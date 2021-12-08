import numpy as np

f = open("C:\\Users\\rick\\Desktop\\advent\\day3\\input.bib", "r")
# f = open("C:\\Users\\rick\\Desktop\\advent\\day3\\test", "r")
Lines = f.readlines()
f.close()

nlines = len(Lines)

arr = []

for j in range(len(Lines)):
    str = Lines[j]
    str = str.replace("\n", "")
    row = []
    for i in range(len(str)):
        row.append(int(str[i]))
    arr.append(row)

input = np.asarray(arr)

res = ""
for i in range(input.shape[1]):
    col = np.sum(input[:, i])
    if col>len(Lines)/2:
        res+="1"
    else:
        res+="0"

a=int(res, 2)
res2 = res
res2 = res2.replace("1", "a")
res2 = res2.replace("0", "1")
res2 = res2.replace("a", "0")
b=int(res2, 2)
print (a*b)


# -----------------------------


f = open("C:\\Users\\rick\\Desktop\\advent\\day3\\input.bib", "r")
# f = open("C:\\Users\\rick\\Desktop\\advent\\day3\\test", "r")
Lines = f.readlines()
f.close()

nlines = len(Lines)

arr = []

for j in range(len(Lines)):
    str = Lines[j]
    str = str.replace("\n", "")
    row = []
    for i in range(len(str)):
        row.append(int(str[i]))
    arr.append(row)

input = np.asarray(arr)
input2 = np.asarray(arr)

res = np.zeros_like(input[0])
for i in range(input.shape[1]):
    col = np.sum(input[:, i])
    if col>=input.shape[0]/2:
        res[i]="1"
        resn = 1
    else:
        res[i]="0"
        resn = 0
    to_delete = []
    for j in range(input.shape[0]):
        if input[j][i] != resn:
            to_delete.append(j)
    if input.shape[0]==1:
        break
    input = np.delete(input, to_delete, axis = 0)

for i in range(input2.shape[1]):
    col = np.sum(input2[:, i])
    if col>=input2.shape[0]/2:
        resn2 = 0
    else:
        resn2 = 1
    to_delete2 = []
    for j in range(input2.shape[0]):
        if input2[j][i] != resn2:
            to_delete2.append(j)
    if input2.shape[0]==1:
        break

    input2 = np.delete(input2, to_delete2, axis = 0)

res = np.array2string(input)
res = res.replace("[", "")
res = res.replace("]", "")
res = res.replace(" ", "")
res2 = np.array2string(input2)
res2 = res2.replace("[", "")
res2 = res2.replace("]", "")
res2 = res2.replace(" ", "")


a=int(res, 2)
b=int(res2, 2)
print (a*b)