from queue import PriorityQueue
import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))

def dijkstra(start, end):
    visited = [-1]*100001
    
    que = PriorityQueue()
    que.put((0, start))

    while not que.empty():
        distance, now = que.get()
        visited[now] = distance

        if now==end:
            break

        move = [[1, now-1]]
        if now<end:
            move.extend([[1, now+1], [0, now*2]])

        for d, i in move:
            if 0<=i<=100000 and visited[i]==-1:
                que.put((distance+d, i))
            
    print(visited[end])
    
dijkstra(N, K)