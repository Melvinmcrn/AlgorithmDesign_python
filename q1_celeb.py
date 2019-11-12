from sys import stdin

n = int(stdin.readline().strip())
data = []
for i in range(n):
    data.append([int(e) for e in stdin.readline().strip().split()])

for i in range(n):
    check = True
    for j in range(n):
        if data[i][j] == 1:
            check = False
            break
    for j in range(n):
        if check == False:
            break
        if data[j][i] == 0 and i!=j:
            check = False
            break

    if check:
        print(i+1)
        break
if check == False:
    print(0)


# totalCol = []
# totalRow = []
# for i in range(n):
#     sumCol = 0
#     sumRow = 0
#     for j in range(n):
#         sumCol += data[j][i]
#         sumRow += data[i][j]
#     totalCol.append(sumCol)
#     totalRow.append(sumRow)

# star = 0
# for i in range(n):
#     if totalCol[i] == n-1 and totalRow[i] == 0:
#         star+=1
# print(star)