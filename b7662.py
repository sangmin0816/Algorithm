from queue import PriorityQueue
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    K = int(input())
    que = PriorityQueue()

    for k in range(K):
        operator, n = map(str, input().split(' '))
        n = int(n)

        if operator=='I':
            que.put(n)
        elif operator == 'D' and not que.empty():
            if n==1:
                que.get()
            else:
                temp = PriorityQueue()
                for i in range(que.qsize()-1):
                    temp.put(que.get())
                que = temp
        
    if que.empty():
        print("EMPTY")
    else:
        print(list(que))
        minimum = que.get()
        for i in range(que.qsize()-1):
            que.get()
        maximum = que.get()
        print(maximum, minimum)