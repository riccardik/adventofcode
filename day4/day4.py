import numpy as np

f = open("C:\\Users\\rick\\Desktop\\advent\\day4\\input.bib", "r")
# f = open("C:\\Users\\rick\\Desktop\\advent\\day4\\test", "r")
Lines = f.readlines()
f.close()

numbers = Lines[0].replace("\n", "").split(",")
numbers = list(map(int, numbers))

del Lines[0]
del Lines[0]

arr = []
for j in range(0, len(Lines), 6):
    bunch = []
    for ii in range(5):
        str1 = Lines[j+ii]
        str1 = str1.replace("\n", "")
        str1 = str1.split()
        row = []
        for i in range(len(str1)):
            row.append(int(str1[i]))
        bunch.append(row)
    print(j)
    arr.append(bunch)

boards = np.asarray(arr)

check = np.zeros_like(boards)
check_prev = np.zeros_like(boards)

try:
    for n in range(len(numbers)):    
        check_prev = np.copy(check)
        for i in range (boards.shape[0]):
            for j in range (boards.shape[1]):
                for k in range (boards.shape[2]):
                    if boards[i][j][k]==numbers[n]:
                        
                        check[i][j][k] = 1
        for i in range (boards.shape[0]):
            for j in range (boards.shape[1]):
                if np.sum(check[i][j][:])==5:
                    print(str(i)+"wons row with"+str(numbers[n]))
                    raise StopIteration
        for i in range (boards.shape[0]):
            for j in range (boards.shape[2]):
                if np.sum(check[i,:,j])==5:
                    print(str(i)+"wons col with"+str(numbers[n]))
                    raise StopIteration
except StopIteration: pass

sum_board = 0
for j in range (boards.shape[1]):
    for k in range (boards.shape[2]):
        if check[i][j][k] == 0:
            sum_board += boards[i][j][k]
print("result= " + str(sum_board*numbers[n]))


check = np.zeros_like(boards)
check_prev = np.zeros_like(boards)
haswon = np.zeros(boards.shape[0])

try:
    for n in range(len(numbers)):    
            check_prev = np.copy(check)
            for i in range (boards.shape[0]):
                for j in range (boards.shape[1]):
                    for k in range (boards.shape[2]):
                        if boards[i][j][k]==numbers[n]:
                            
                            check[i][j][k] = 1
            for i in range (boards.shape[0]):
                for j in range (boards.shape[1]):
                    if np.sum(check[i][j][:])==5:
                        # print(str(i)+"wons row with"+str(numbers[n]))
                        haswon[i] = 1
                        if  np.sum(haswon)==boards.shape[0]:
                            raise StopIteration
            for i in range (boards.shape[0]):
                for j in range (boards.shape[2]):
                    if np.sum(check[i,:,j])==5:
                        # print(str(i)+"wons col with"+str(numbers[n]))
                        haswon[i] = 1
                        if  np.sum(haswon)==boards.shape[0]:
                            raise StopIteration
except StopIteration: pass

sum_board = 0
for j in range (boards.shape[1]):
    for k in range (boards.shape[2]):
        if check[i][j][k] == 0:
            sum_board += boards[i][j][k]
print("board "+str(i)+" result= " + str(sum_board*numbers[n]))