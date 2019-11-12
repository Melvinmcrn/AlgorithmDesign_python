from sys import stdin

matrix = list()

def checkInvalid(r1,c1,r2,c2):
    if r1>r2 or c1>c2:
        return True
    return False

def checkOutside(r1,c1,r2,c2):
    if r1>n or r2<=0 or c1>m or c2<=0:
        return True
    return False

n,m = [int(e) for e in stdin.readline().strip().split()]
r = int(stdin.readline().strip())

for i in range(n):
    matrix.append([int(e) for e in stdin.readline().strip().split()])

for i in range(r):
    r1,c1,r2,c2 = [int(e) for e in stdin.readline().strip().split()]
    if checkInvalid(r1,c1,r2,c2):
        print("INVALID")
    elif checkOutside(r1,c1,r2,c2):
        print("OUTSIDE")
    else:
        if r1<=0:
            r1 = 1
        if r2>n:
            r2 = n
        if c1<=0:
            c1 = 1
        if c2>m:
            c2 = m
        out = -10000000000000000
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                if matrix[i-1][j-1] > out:
                    out = matrix[i-1][j-1]
        print(out)