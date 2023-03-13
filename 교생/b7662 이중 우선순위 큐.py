from queue import PriorityQueue
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    K = int(input())
    min_que = PriorityQueue()
    max_que = PriorityQueue()
    visit = dict()
    que_len = 0

    for k in range(K):
        op, num = map(str, input().split(' '))
        num = int(num)

        if op=='I':
            min_que.put(num)
            max_que.put(-num)
            if num not in visit:
                visit[num] = 0
            visit[num] += 1
            que_len += 1
        elif que_len>0:
            que_len -= 1
            if num==-1:
                while True:
                    temp = min_que.get()
                    if visit[temp]>0:
                        visit[temp]-=1
                        break
            else:
                while True:
                    temp = -max_que.get()
                    if visit[temp]>0:
                        visit[temp]-=1
                        break
    
    if que_len==0:
        print("EMPTY")
    else:
        while True:
            maximum = -max_que.get()
            if visit[maximum]>0:
                print(maximum, end=' ')
                break
        while True:
            minimum = min_que.get()
            if visit[minimum]>0:
                print(minimum, end=' ')
                break
        
