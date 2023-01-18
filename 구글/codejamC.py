from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    S = list(map(int, input().split(' ')))

    S.sort() # 아랫줄과 순서가 바껴서 틀림
    dice = deque([S[0]])

    for s in range(1, len(S)):
        if S[s] <= dice[-1]:
            if dice[0]>1:
                dice.appendleft(dice[0]-1)
        else:
            dice.append(dice[-1]+1)
    
    print('Case #%d: ' %(t+1), end='')
    print(len(set(dice)))
