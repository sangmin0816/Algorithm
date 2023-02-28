import sys
input = sys.stdin.readline

M, N = map(int, input().split(' '))
snacks = list(map(int, input().split(' ')))

def bin_search(arr, key, low, high):
    ans = list()

    while low<=high:
        mid = (low+high)//2
        temp = 0

        for a in arr:
            if a >= mid and mid!=0:
                temp += a//mid
        
        if temp>=key:
            ans.append(mid)
            low = mid+1
        else:
            high = mid-1
    
    if ans:
        return max(ans)
    else:
        return 0

print(bin_search(snacks, M, 0, max(snacks)+1))