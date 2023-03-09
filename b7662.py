import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    K = int(input())
    que = list()

    for k in range(K):
        operator, n = map(str, input().split(' '))
        n = int(n)
        
        if operator=='I':
            que.append(n)
        elif operator == 'D' and len(que):
            if n==1:
                que.pop()
            else:
                que = que[1:]
        
        que.sort()
        
    if not len(que):
        print("EMPTY")
    else:
        minimum = min(que)
        maximum = max(que)
        print(maximum, minimum)