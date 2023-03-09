# 무려 16번만에 성공..
from queue import PriorityQueue
import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))

jewels = PriorityQueue()
for n in range(N):
    M, V = map(int, input().split(' '))
    jewels.put([M, V])

bags = list()
for k in range(K):
    bags.append(int(input()))

bags.sort()

ans = 0

temp = PriorityQueue()
for b in bags:
    while not jewels.empty():
        M, V = map(int, jewels.get())
        if M<=b:
            temp.put(-V)
        else:
            jewels.put([M, V])
            break
    if not temp.empty():
        ans += -temp.get()

print(ans)