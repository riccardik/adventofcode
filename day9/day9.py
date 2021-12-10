import numpy as np


# f = open("C:\\Users\\rick\\Desktop\\advent\\day9\\input.bib", "r")
f = open("C:\\Users\\rick\\Desktop\\advent\\day9\\test", "r")
Lines = f.readlines()
f.close()

input = []
for i in range(len(Lines)):
    line = Lines[i].replace("\n", "")
    row = []
    for j in range(len(line)):
        row.append(int(line[j]))
    input.append(row)

input_arrr = np.asarray(input)
input_arr = np.ones([input_arrr.shape[0]+2, input_arrr.shape[1]+2])*9
input_arr[1:input_arrr.shape[0]+1, 1:input_arrr.shape[1]+1] = input_arrr
weight = np.zeros_like(input_arrr)
for i in range(1, input_arr.shape[0]-1):
    for j in range(1, input_arr.shape[1]-1):
        if (input_arr[i, j]<input_arr[i, j-1]) and (input_arr[i, j]<input_arr[i, j+1]) and (input_arr[i, j]<input_arr[i+1, j]) and (input_arr[i, j]<input_arr[i-1, j]):
            
            weight[i-1, j-1] = input_arrr[i-1, j-1] + 1 
            
print(np.sum(weight))

# ---------------------

peaks = np.zeros_like(input_arr)
for i in range(input_arr.shape[0]):
    for j in range(input_arr.shape[1]):
        if input_arr[i][j] == 9: 
            peaks[i][j] = 1
        