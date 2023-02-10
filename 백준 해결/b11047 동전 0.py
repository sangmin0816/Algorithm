import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))

coins = list()
for n in range(N):
    coins.append(int(input()))

ans = 0

while coins:
    now = coins.pop()
    if now<=K:
        ans += K//now
        K %= now
    if K==0:
        print(ans)
        break