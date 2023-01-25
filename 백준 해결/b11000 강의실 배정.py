import sys
input = sys.stdin.readline
from queue import PriorityQueue

N = int(input())
lectures = list()

for n in range(N):
    S, T = map(int, input().split(' '))
    lectures.append([S, T])
    
lectures.sort()

classroom = PriorityQueue()
classroom.put(lectures[0][1])

for i in range(1, N):
    temp = classroom.get()
    if lectures[i][0] < temp:
        classroom.put(temp)
    classroom.put(lectures[i][1])

print(classroom.qsize())
        