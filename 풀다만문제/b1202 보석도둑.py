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

jewels.sort(key=lambda x:(-x[0], x[1]))
bags.sort()

for b in bags:
    while jewels:
        if jewels[-1][0]<=b:
            ans+=jewels.pop()[1]
        else:
            break

print(ans)