from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    I1 = deque(input())
    I2 = deque(input())
    result =0

    for i in I1:
        while(len(I2)):
            if i == I2[0]:
                I2.append(I2.popleft())
                break
            else:
                result+=1
                I2.popleft()
    
    if len(I1) != len(I2):
        result = "IMPOSSIBLE"

    print("Case #", end='')
    print(t+1, end='')
    print(": ", end='')
    print(result)