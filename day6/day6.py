import numpy as np

f = open("C:\\Users\\rick\\Desktop\\advent\\day6\\test", "r")
f = open("C:\\Users\\rick\\Desktop\\advent\\day6\\input.bib", "r")
Lines = f.readlines()
f.close()

initial_state = Lines[0].split(",")
initial_state = [int(initial_state[x]) for x in range(len(initial_state))]
state = np.asarray(initial_state)

counter = 0
while counter<=17:
    counter+=1
    to_add = 0
    
    for i in range(state.shape[0]):
        if state[i] == 0:
            state[i] = 7
            to_add+=1
    state -=1
    for i in range(to_add):
        state = np.append(state, 8)
    # print(state)
    # input()

print(state.shape[0])

#-------------

fishes = [0 for x in range(9)]


for i in range(len(initial_state)):
    fishes[initial_state[i]]+=1

counter=0
while counter<=255:
    counter+=1
    to_add = fishes[0]
    for i in range(1, len(fishes)):
        fishes[i-1] = fishes[i]
    fishes[8] = to_add
    fishes[6] = fishes[6] + to_add
    # print(fishes)
    # input()
   


    
    
sum = 0
for i in range (len(fishes)):
    sum+=fishes[i]
print(sum)