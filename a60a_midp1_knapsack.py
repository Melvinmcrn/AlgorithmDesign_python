from sys import stdin

n,m = [int(e) for e in stdin.readline().strip().split()]
v = [0] + [int(e) for e in stdin.readline().strip().split()]
w = [0] + [int(e) for e in stdin.readline().strip().split()]
data = []

for i in range(n+1):
        data.append([int(e) for e in stdin.readline().strip().split()])

out = []

for i in range(n,0,-1):
    if data[i][m]!=data[i-1][m]:
        out.append(i)
        m -= w[i]

print(len(out))
outstr = ""
for c in out:
    outstr += str(c) + " "

print(outstr.strip())