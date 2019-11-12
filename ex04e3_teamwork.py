from sys import stdin as kb

n,m = [int(e) for e in kb.readline().strip().split()]
sub = [int(e) for e in kb.readline().strip().split()]
sub.sort()

totalTime = 0
student = [0] * n

for i in range(m):
    (student.sort())
    student[0] += sub[i]
    totalTime += student[0]
    #print(totalTime)

print(round(totalTime/m, 3))