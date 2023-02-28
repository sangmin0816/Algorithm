import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
trees = list(map(int, input().split(' ')))

def bin_search(key, arr, low, high):
    while low<=high:
        mid = (low+high)//2
        temp = 0
        for a in arr:
            if a>mid:
                temp += a-mid
        
        if temp==key:
            return mid
        elif temp > key:
            low = mid+1
        else:
            high =  mid-1

    return high

print(bin_search(M, trees, 0, max(trees)))