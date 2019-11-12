from sys import stdin as kb
import queue

r,c = [int(e) for e in kb.readline().strip().split()]

table = []
reach = []
for i in range(r):
    pim = kb.readline().strip()
    table.append([])
    reach.append([])
    for x in pim:
        if x == '.':
            reach[-1].append(False)
        else:
            reach[-1].append(True)
        table[-1].append(-1)

q = queue.Queue()

q.put((0,0))
reach[0][0] = True
table[0][0] = 0

while not q.empty():
    position = q.get()
    top = (position[0]-1,position[1])
    btm = (position[0]+1,position[1])
    lft = (position[0],position[1]-1)
    rgt = (position[0],position[1]+1)

    if top[0] >= 0:
        if not reach[top[0]][top[1]]:
            reach[top[0]][top[1]] = True
            table[top[0]][top[1]] = table[position[0]][position[1]] + 1
            q.put(top)
    if btm[0] < r:
        if not reach[btm[0]][btm[1]]:
            reach[btm[0]][btm[1]] = True
            table[btm[0]][btm[1]] = table[position[0]][position[1]] + 1
            q.put(btm)

    if lft[1] >= 0:
        if not reach[lft[0]][lft[1]]:
            reach[lft[0]][lft[1]] = True
            table[lft[0]][lft[1]] = table[position[0]][position[1]] + 1
            q.put(lft)
    if rgt[1] < c:
        if not reach[rgt[0]][rgt[1]]:
            reach[rgt[0]][rgt[1]] = True
            table[rgt[0]][rgt[1]] = table[position[0]][position[1]] + 1
            q.put(rgt)
print(table[-1][-1])