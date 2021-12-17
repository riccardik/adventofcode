import numpy as np

# f = open("C:\\Users\\rick\\Desktop\\advent\\day11\\input.bib", "r")
f = open("C:\\Users\\rick\\Desktop\\advent\\day11\\test", "r")
Lines = f.readlines()
f.close()

arr = []

for j in range(len(Lines)):
    str = Lines[j]
    str = str.replace("\n", "")
    row = []
    for i in range(len(str)):
        row.append(int(str[i]))
    arr.append(row)

in_arr = np.asarray(arr)
flashes = 0
for jj in range(100):
    in_arr = in_arr+1
    input_arr = np.zeros([in_arr.shape[0]+4, in_arr.shape[1]+4])
    input_arr[2:in_arr.shape[0]+2, 2:in_arr.shape[1]+2] = in_arr
    calculated = 1
    map = np.zeros_like(input_arr)
    while(calculated!=0):
        calculated = 0        
        for i in range(2, input_arr.shape[0]-2):
            for j in range(2, input_arr.shape[1]-2):
                if input_arr[i][j]>9 and map[i][j]==0:
                    input_arr[i+1][j+1] += 1
                    input_arr[i+1][j-1] += 1
                    input_arr[i-1][j+1] += 1
                    input_arr[i-1][j-1] += 1
                    input_arr[i][j-1] += 1
                    input_arr[i][j+1] += 1
                    input_arr[i+1][j] += 1
                    input_arr[i-1][j] += 1
                    # input_arr[i+2][j+2] += 1
                    # input_arr[i+2][j-2] += 1
                    # input_arr[i-2][j+2] += 1
                    # input_arr[i-2][j-2] += 1
                    calculated+=1
                    map[i][j]=1
                    
    in_arr = input_arr[2:in_arr.shape[0]+2,2:in_arr.shape[1]+2]
    for i in range(in_arr.shape[0]):
        for j in range(in_arr.shape[1]):
            if in_arr[i][j]>9:
                in_arr[i][j] = 0
                flashes +=1
    # print(in_arr)
    # input()
print(flashes)

# --------------------------

in_arr = np.asarray(arr)
flashes = 0
found = 0
steps = 0
while found==0:
    steps +=1
    in_arr = in_arr+1
    input_arr = np.zeros([in_arr.shape[0]+4, in_arr.shape[1]+4])
    input_arr[2:in_arr.shape[0]+2, 2:in_arr.shape[1]+2] = in_arr
    calculated = 1
    map = np.zeros_like(input_arr)
    while(calculated!=0):
        calculated = 0        
        for i in range(2, input_arr.shape[0]-2):
            for j in range(2, input_arr.shape[1]-2):
                if input_arr[i][j]>9 and map[i][j]==0:
                    input_arr[i+1][j+1] += 1
                    input_arr[i+1][j-1] += 1
                    input_arr[i-1][j+1] += 1
                    input_arr[i-1][j-1] += 1
                    input_arr[i][j-1] += 1
                    input_arr[i][j+1] += 1
                    input_arr[i+1][j] += 1
                    input_arr[i-1][j] += 1
                    # input_arr[i+2][j+2] += 1
                    # input_arr[i+2][j-2] += 1
                    # input_arr[i-2][j+2] += 1
                    # input_arr[i-2][j-2] += 1
                    calculated+=1
                    map[i][j]=1
                    
    in_arr = input_arr[2:in_arr.shape[0]+2,2:in_arr.shape[1]+2]
    for i in range(in_arr.shape[0]):
        for j in range(in_arr.shape[1]):
            if in_arr[i][j]>9:
                in_arr[i][j] = 0
                flashes +=1
    # print(in_arr)
    # input()
    if np.sum(in_arr) == np.sum(np.zeros_like(in_arr)):
        found = 1
print(steps)