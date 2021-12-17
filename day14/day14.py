import numpy as np

# f = open("C:\\Users\\rick\\Desktop\\advent\\day14\\input.bib", "r")
f = open("C:\\Users\\rick\\Desktop\\advent\\day14\\test", "r")
Lines = f.readlines()
f.close()

initial = Lines[0].replace("\n", "")
del Lines[0]
del Lines[0]

Lines = [Lines[x].split(" -> ") for x in range(len(Lines))]
subst = [[Lines[x][0], Lines[x][1].replace("\n", "") ] for x in range(0, len(Lines))]

composite = initial
for i in range(40):
    to_add = []
    for j in range(len(composite)-1):
        par_ = composite[j]+composite[j+1]
        for jj in range(len(subst)):
            if par_==subst[jj][0]:
                to_add.append(subst[jj][1])
    for j in range(len(to_add)):

        composite = composite[:j+1+j] + to_add[j] + composite[j+1+j:]
    print(i)
# [B, C, H, N]

# count = [0,0,0,0]

# for i in range(len(composite)):
#     if composite[i] == 'B':
#         count[0] +=1
#     elif composite[i] == 'C':
#         count[1] +=1
#     elif composite[i] == 'H':
#         count[2] +=1
#     elif composite[i] == 'N':
#         count[3] +=1
# count.sort()
# print(count[3]-count[0])


letter_count = []
counts_dict = {}
for c in list(composite):
  if c not in counts_dict:
    counts_dict[c] = 0
  counts_dict[c] += 1

for key, value in counts_dict.items():
    letter_count.append([key, composite.count(key)])
letter_count = np.asarray(letter_count)[:, 1]
letter_count = np.sort(np.asarray(letter_count, dtype=int))
print(letter_count[letter_count.shape[0]-1]-letter_count[0])