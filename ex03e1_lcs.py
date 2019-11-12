from sys import stdin

a = list(stdin.readline().strip())
b = list(stdin.readline().strip())

data = [[0 for e in range(len(a)+1)]]
for i in range(len(b)+1):
    data.append([0])

for i in range(1,len(b)+1):
    for j in range(1,len(a)+1):
        if a[j-1] == b[i-1]:
            data[i].append(data[i-1][j-1]+1)
        else:
            data[i].append(max(data[i-1][j],data[i][j-1]))
print(data[len(b)][len(a)])