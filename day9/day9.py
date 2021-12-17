import numpy as np


# f = open("C:\\Users\\rick\\Desktop\\advent\\day9\\input.bib", "r")
f = open("C:\\Users\\rick\\Desktop\\advent\\day9\\test", "r")
Lines = f.readlines()
f.close()

input_f = []
for i in range(len(Lines)):
    line = Lines[i].replace("\n", "")
    row = []
    for j in range(len(line)):
        row.append(int(line[j]))
    input_f.append(row)

input_arrr = np.asarray(input_f)
input_arr = np.ones([input_arrr.shape[0]+2, input_arrr.shape[1]+2])*9
input_arr[1:input_arrr.shape[0]+1, 1:input_arrr.shape[1]+1] = input_arrr
weight = np.zeros_like(input_arrr)
for i in range(1, input_arr.shape[0]-1):
    for j in range(1, input_arr.shape[1]-1):
        if (input_arr[i, j]<input_arr[i, j-1]) and (input_arr[i, j]<input_arr[i, j+1]) and (input_arr[i, j]<input_arr[i+1, j]) and (input_arr[i, j]<input_arr[i-1, j]):
            
            weight[i-1, j-1] = input_arrr[i-1, j-1] + 1 
            
print(np.sum(weight))

# ---------------------

def check_vis(peaks, i, j, n): 
    
            
                peaks[i][j] = id_b
                if (peaks[i][j-1] != 1) and (peaks[i][j-1] != n):
                    peaks[i][j-1] = n
                    check_vis(peaks, i, j-1, n)
                if (peaks[i][j+1] != 1) and (peaks[i][j+1] != n):
                    peaks[i][j+1] = n
                    check_vis(peaks, i, j+1, n)
                if (peaks[i-1][j] != 1) and (peaks[i-1][j] != n):
                    peaks[i-1][j] = n
                    check_vis(peaks, i-1, j, n)
                if (peaks[i+1][j] != 1) and (peaks[i+1][j] != n):
                    peaks[i+1][j] = n
                    check_vis(peaks, i+1, j, n)


peaks = np.zeros_like(input_arr)
for i in range(input_arr.shape[0]):
    for j in range(input_arr.shape[1]):
        if input_arr[i][j] == 9: 
            peaks[i][j] = 1
id_b = 2
for i in range(peaks.shape[0]):
    for j in range(peaks.shape[1]):
            if peaks[i][j] != 1: 
                if peaks[i][j] == 0:
                    check_vis(peaks, i, j, id_b)
                    id_b +=1
                # print(peaks)
                # input()

blobs = peaks[1:peaks.shape[0]-1, 1:peaks.shape[1]-1]-1

size = []            
for i in range(int(np.max(blobs))):
    res = 1*(blobs == i+1) 
    size.append(int(np.sum(res)))
size.sort(reverse=True)
print(size[0]*size[1]*size[2])