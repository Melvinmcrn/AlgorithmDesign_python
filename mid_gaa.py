from sys import stdin

def findGAA(x, n, length):
    if n == 0:
        if x == 1:
            return 'g'
        return 'a'

    slength = (length - (n+3))/2

    if x <= slength:
        return findGAA(x, n-1, slength)
    x -= slength
    if x <= n+3:
        if x == 1:
            return 'g'
        return 'a'
    x -= (n+3)
    return findGAA(x, n-1, slength)
    
n = int(stdin.readline().strip())
print(findGAA(n, 27, 1073741792))
