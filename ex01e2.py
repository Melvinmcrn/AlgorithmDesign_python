from sys import stdin

n = int(stdin.readline().strip())
data = [0] + [int(e) for e in stdin.readline().strip().split()]
temp = [0] + [data[1]]
for i in range(2,len(data)):
    temp.append(temp[i-1]+data[i])
    
most = -99999999999999999
for i in range(len(data)-2):
    for j in range(i+1,len(data)):
        if temp[j] - temp[i] > most:
            most = temp[j]-temp[i]
print(most)