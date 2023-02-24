import sys
input = sys.stdin.readline

N, T = map(int, input().split(' '))

bus = list()
for n in range(N):
    start, gap, num = map(int, input().split(' '))
    for i in range(1, num+1):
        bus.append(start+gap*i)

bus.sort()

def bin_serch(bus, key, low, mid, high):
    if key == bus[mid]:
        return True
    if low>high:

if T > bus[-1]:
    print(-1)
else:
