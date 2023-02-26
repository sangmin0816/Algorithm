from queue import PriorityQueue
import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))
jewels = PriorityQueue()

for n in range(N):
    M, V = map(int, input().split(' '))
    jewels.put((-V, M))

bags = list()
for k in range(K):
    bags.append(int(input()))

ans = 0

bags.sort(reverse=True)
temp = PriorityQueue()

for b in bags:
    for i in range(jewels.qsize()):
        v, m = jewels.get()
        if m<=b:
            ans += -v
            break
        temp.put([v, m])
    jewels.join(temp)

print(ans)