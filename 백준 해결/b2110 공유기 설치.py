import sys
input = sys.stdin.readline

N, C = map(int, input().split(' '))
houses = [int(input()) for n in range(N)]
houses.sort()

def bin_search(arr, key, low, high):
    ans = []
    while low<=high:
        mid = (low+high)//2
        temp = 1
        coo = min(arr)

        for a in arr:
            if coo+mid<=a:
                temp+=1
                coo = a

        if temp>=key:
            low = mid+1
            ans.append(mid)
        else:
            high = mid-1
    
    return max(ans)

print(bin_search(houses, C, 0, houses[-1]))