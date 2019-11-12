from sys import stdin

temp = dict()

def calculate(x,n,k):

    if n<5:
        return (x**n)%k

    left = n//2
    right = n-left

    if (x,left,k) in temp:
        leftValue = temp[(x,left,k)]
    else:
        leftValue = calculate(x,left,k)
        temp[(x,left,k)] = leftValue

    if (x,right,k) in temp:
        rightValue = temp[(x,right,k)]
    else:
        rightValue = calculate(x,right,k)
        temp[(x,right,k)] = rightValue

    return (leftValue*rightValue)%k

x,n,k = [int(e) for e in stdin.readline().strip().split()]
print(calculate(x,n,k))
