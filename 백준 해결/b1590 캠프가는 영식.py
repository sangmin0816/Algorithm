import sys
input = sys.stdin.readline

N, T = map(int, input().split(' '))

bus = list()
for n in range(N):
    start, gap, num = map(int, input().split(' '))
    for i in range(num):
        bus.append(start+gap*i)

bus.sort()

def bin_search(bus, key, low, high):

    while low<=high:
        mid = (low+high)//2

        if key==bus[mid]:
            return key
        elif key > bus[mid]:
            low = mid+1
        elif key < bus[mid]:
            high = mid-1
    
    return bus[low]

if T > bus[-1]:
    print(-1)
else:
    print(bin_search(bus, T, 0, len(bus)-1)-T)
