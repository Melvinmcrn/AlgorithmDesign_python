from sys import stdin
kb = stdin

memory = dict()

def c(n,k):
    if n==k or k==0:
        return 1
    else:
        if (n-1,k-1) in memory:
            x = memory[(n-1,k-1)]
        else:
            x = c(n-1,k-1)
            memory[(n-1,k-1)] = x
        if (n-1,k) in memory:
            y = memory[(n-1,k)]
        else:
            y = c(n-1,k)
            memory[(n-1,k)] = y
        return x + y

n,k = [int(e) for e in kb.readline().split()]
memory = dict()
print(c(n,k))