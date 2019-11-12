from sys import stdin

n,m,k = [int(e) for e in stdin.readline().split()]
data = []
data2 = []

for i in range(n):
    temp = [int(e) for e in stdin.readline().split()]
    data.append(temp)

data2.append([data[0][0]])

for i in range(1,m):
    data2[0].append(data[0][i] + data2[0][i-1])

for i in range(1,n):
    data2.append([data[i][0] + data2[i-1][0]])
    for j in range(1,m):
        data2[i].append(data2[i-1][j] + data2[i][j-1] + data[i][j] - data2[i-1][j-1])

for i in range(k):
    r1,c1,r2,c2 = [int(e) for e in stdin.readline().split()]
    r1-=1
    c1-=1
    if r1 < 0 and c1 < 0:
        print(data2[r2][c2])
    elif r1 < 0:
        print(data2[r2][c2] - data2[r2][c1])
    elif c1 < 0:
        print(data2[r2][c2] - data2[r1][c2])
    else:
        print(data2[r2][c2] - data2[r2][c1] - data2[r1][c2] + data2[r1][c1])