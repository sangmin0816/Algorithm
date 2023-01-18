from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
line = deque(list(map(int, input().split(' '))))

temp = list()

first = 1
while(len(line)):
    if first == line[0]:
        line.popleft()
        first+=1
        continue
    elif len(temp) and first == temp[len(temp)-1]:
        first+=1
        temp.pop()
        continue
    else:
        temp.append(line.popleft())

while(len(temp)):
    if first == temp.pop():
        first+=1

if first == N+1:
    print("Nice")
else:
    print("Sad")