from sys import stdin as kb

n,e = [int(e) for e in kb.readline().strip().split()]

data = dict()

for i in range(e):
    a,b = [int(e) for e in kb.readline().strip().split()]
    if b not in data:
        data[b] = {a}
    else:
        data[b].add(a)
#print(data)

for i in range(5):
    temp = [int(e) for e in kb.readline().strip().split()]
    tempSet = set()
    check = True
    for c in temp:
        if c in data:
            #print("dif = " +str(data[c]-tempSet))
            if data[c] - tempSet != set():
                print("FAIL")
                check = False
                break
        tempSet.add(c)        

    if check:
        print('SUCCESS')