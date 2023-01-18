# K번 89
from collections import deque
import sys
input = sys.stdin.readline

bracket = deque(input().strip())

ans = 0

temp = deque()

for i in bracket:
    if(i=='('):
        temp.append(i)
    elif(len(temp)):
        cnt = 1
        while(temp.pop() =='Y'):
            cnt += 1
        
        ans = ans + cnt
        temp.append('Y')
        
print(ans)