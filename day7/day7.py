import numpy as np
import math 
f = open("C:\\Users\\rick\\Desktop\\advent\\day7\\test", "r")
# f = open("C:\\Users\\rick\\Desktop\\advent\\day7\\input.bib", "r")
Lines = f.readlines()
f.close()

line = Lines[0].split(",")
line = [int(line[x]) for x in range(len(line))]
positions = np.asarray(line)
ordered_positions = np.asarray(list(range(0, positions.max()+1)))
fuel_cost = np.zeros_like(ordered_positions)


for i in range(ordered_positions.shape[0]):
    for j in range(positions.shape[0]):
        fuel_cost[i] += math.sqrt(math.pow(positions[j] - ordered_positions[i], 2))
print(fuel_cost.min())

# --------------------------------
# fuel_cost = np.zeros_like(ordered_positions)

# for i in range(ordered_positions.shape[0]):
#     print(i)
#     for j in range(positions.shape[0]):
#         step = int(math.sqrt(math.pow(positions[j] - ordered_positions[i], 2)))
#         total_steps = 0
#         # print(step)      
#         for jj in range(step):
#             total_steps += jj+1
#             # print(total_steps)
#             # input()
#         # print(total_steps)
#         fuel_cost[i] += total_steps
# print(fuel_cost)      
# print(fuel_cost.min())


min_fuel_cost = float('inf')

for i in range(ordered_positions.shape[0]):
    print(i)
    fuel_cost2= 0
    for j in range(positions.shape[0]):
        step = int(math.sqrt(math.pow(positions[j] - ordered_positions[i], 2)))
        total_steps = 0    
        for jj in range(step):
            total_steps += jj+1
        fuel_cost2 += total_steps
    if fuel_cost2<min_fuel_cost:
        min_fuel_cost=fuel_cost2
print(min_fuel_cost)
    
        
        
