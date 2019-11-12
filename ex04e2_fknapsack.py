from sys import stdin as kb

w,n = [float(e) for e in kb.readline().strip().split()]
n = int(n)
value = [float(e) for e in kb.readline().strip().split()]
weight = [float(e) for e in kb.readline().strip().split()]
data = dict()
totalPrice = 0
for i in range(n):
    if weight[i] != 0:
        data[value[i] / weight[i]] = (value[i],weight[i])
    else:
        totalPrice += value[i]

totalWeight = 0
for c in sorted(data.keys(), reverse = True):
    if w <= totalWeight:
        break

    wLeft = w - totalWeight
    if data[c][1] <= wLeft:
        totalPrice += data[c][0]
        totalWeight += data[c][1]
    elif data[c][1] > wLeft:
        totalPrice += c * (wLeft)
        break
print(round(totalPrice,4))