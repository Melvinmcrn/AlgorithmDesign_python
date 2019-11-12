from sys import stdin

n,m = [int(e) for e in stdin.readline().strip().split()]

forest = []
score = []

for i in range(n):
    forest.append([int(e) for e in stdin.readline().strip().split()])

for i in range(n+1):
    score.append([])
    for j in range(m+1):
        if i==0 or j==0:
            score[i].append(0)
        else:
            most = max(score[i-1][j-1], score[i-1][j], score[i][j-1])
            if score[i-1][j-1]+2*forest[i-1][j-1] > most+forest[i-1][j-1] and i-1 > 0 and j-1 > 0:
                score[i].append(score[i-1][j-1]+2*forest[i-1][j-1])

            elif most == score[i-1][j-1] and i-1 > 0 and j-1 > 0:
                score[i].append(score[i-1][j-1])

            else:
                score[i].append(most + forest[i-1][j-1])

print(score[n][m])