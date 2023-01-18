import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    S = list(input().rstrip())
    ans = 0

    for i in range(N-1):
        for j in range(i+5, N):
            if S[i] != S[j]:

    print("Case #", end='')
    print(t+1, end='')
    print(": ", end='')
    print(result)