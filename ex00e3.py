from sys import stdin

n = int(stdin.readline().strip())
data = [False]*n
number = [int(e) for e in stdin.readline().strip().split()]

check = True
for c in number:
    if c < 1:
        print("NO")
        check = False
        break
    elif c > n:
        print("NO")
        check = False
        break
    elif data[c-1]:
        print("NO")
        check = False
        break
    else:
        data[c-1] = True
if check:
    print("YES")
