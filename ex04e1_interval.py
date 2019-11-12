from sys import stdin as kb

n = int(kb.readline().strip())
s = [int(e) for e in kb.readline().strip().split()]
f = [int(e) for e in kb.readline().strip().split()]
data = dict()

for i in range(n):
    if f[i] not in data:
        data[f[i]] = s[i]
    elif s[i] > data[f[i]]:
            data[f[i]] = s[i]

count = 0
time = -1
for c in sorted(data.keys()):
    if data[c] >= time:
        time = c
        count += 1

print(count)