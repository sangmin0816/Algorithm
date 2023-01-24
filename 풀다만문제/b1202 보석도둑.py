import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))
jewels = list()

for n in range(N):
    jewels.append(list(map(int, input().split(' '))))

bags = list()
for k in range(K):
    bags.append(int(input()))

ans = 0

jewels.sort(key=lambda x:x[1], reverse=True)
bags.sort()

for M, V in jewels:
    for bag in bags:
        if bag >= M:
            ans += V
            bags.pop(bags.index(bag))
            break

print(ans)