import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))

jewels = list()
for n in range(N):
    M, V = map(int, input().split(' '))
    jewels.append([V, M])

bags = list()
for k in range(K):
    bags.append(int(input()))

ans = 0

bags.sort(reverse=True)

temp = list()

for b in bags:
    jewels.sort(key=lambda x:(x[0], x[1]))
    while jewels:
        v, m = jewels.pop()
        if m<=b:
            ans+=v
            break
        temp.append([v, m])
    
    jewels.extend(temp)

print(ans)