from sys import stdin as kb

time = 0

def intoTheMap(x):

    print('now i"m ' + str(x))
    if color[x] != 'w':
        return
        
    global time
    time = time + 1

    s[x] = time
    color[x] = 'g'

    for c in data[x]:
        print(str("get into ") + str(c))
        intoTheMap(c)

    time += 1
    f[x] = time
    color[x] = 'b'
    return



n = int(kb.readline().strip())

color = []
s = []
f = []
for i in range(n):
    s.append(0)
    f.append(0)
    color.append('w')

data = [[int(e) for e in kb.readline().strip().split()[1:]] for d in range(n)]
#print(data)

time = 0
for i in range(n):
    intoTheMap(i)
print(data)
print(s)
print(f)