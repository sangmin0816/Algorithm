from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N = input().strip()
    Narr = deque(map(int, N))

    if(sum(Narr)%9!=0):
        n = 9 - sum(Narr)%9
        if len(Narr) == 1 and Narr[0]>n:
            Narr.appendleft(n)
        else:
            Narr.append(n)
            
    result = ""
    for i in Narr:
        result = result + chr(ord('0')+i)

    print("Case #", end='')
    print(t, end='')
    print(": ", end='')
    print(str(result))
