import sys
input = sys.stdin.readline

def bin_search(key, low, high):
    while low<high:
        mid = (low+high)//2

        new_Z = int((Y+mid)/(X+mid)*100)
        if new_Z > key:
            high = mid-1
        else:
            low = mid+1

    return low

X, Y = map(int, input().split(' '))
if X==Y:
    print(-1)
else:
    Z = int(Y/X*100)
    print(bin_search(Z, 0, X))