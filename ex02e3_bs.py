import sys
kb = sys.stdin

def binarySearch(number, l, r, data):
    mid = (l+r)//2
    #print("number = "+str(number))
    #print(data)
    #print("l = "+str(l)+" r = "+str(r)+" mid = "+str(mid))
    if l > r:
        #print("***** 1 *****")
        return -1
    elif l == r and data[l] <= number:
        #print("***** 2 *****")
        return l
    elif data[mid] <= number and data[mid+1] > number:
        #print("***** 3 *****")
        return mid
    elif data[mid] > number:
        #print("***** 4 *****")
        return binarySearch(number, l, mid-1, data)
    else:
        #print("***** 5 *****")
        return binarySearch(number, mid+1, r, data)

n,m = [int(e) for e in kb.readline().split()]
n_array = [int(e) for e in kb.readline().split()]
m_array = [int(e) for e in kb.readline().split()]

for c in m_array:
        if c < n_array[0]:
            print(-1)
        else:
            print(binarySearch(c, 0, len(n_array)-1, n_array))