import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
cards = list(map(int, input().split(' ')))
ans = []

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            black_jack = cards[i]+cards[j]+cards[k]
            if black_jack==M:
                print(M)
                sys.exit(0)
            elif black_jack < M:
                ans.append(black_jack)

print(max(ans))