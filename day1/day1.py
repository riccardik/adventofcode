f = open("C:\\Users\\rick\\Desktop\\advent\\day1\\input.bib", "r")
f = open("C:\\Users\\rick\\Desktop\\advent\\day1\\test.txt", "r")
Lines = f.readlines()
f.close()


for i in range(len(Lines)):
    Lines[i] = Lines[i].replace("\n", "")
    Lines[i] = Lines[i].replace(" ", "")

count=0
for i in range(1, len(Lines)):
    if int(Lines[i])>int(Lines[i-1]):
        count+=1
print(count)

count=0
prevsum = float('inf')
for i in range(2 , len(Lines)):
    # print(i)
    sum = int(Lines[i])+int(Lines[i-1])+int(Lines[i-2])
    
    # print(prevsum)
    # print(sum)
    # input()
    if sum>prevsum:
        count+=1
        print ("increased")
    prevsum = sum
print(count)