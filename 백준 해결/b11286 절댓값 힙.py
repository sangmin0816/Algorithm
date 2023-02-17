from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())
que = PriorityQueue()

for n in range(N):
    x = int(input())
    if x==0:
        if que.empty():
            print(0)
        else:
            print(que.get()[1])
    else:
        que.put((abs(x), x))
