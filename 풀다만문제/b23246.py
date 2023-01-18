import sys
input = sys.stdin.readline

N = int(input())

athletes = list()
for n in range(N):
    b, p, q, r = map(int, input().split(' '))
    athletes.append([p*q*r, p+q+r, b])

athletes.sort()

for i in range(3):
    print(athletes[i][2], end=' ')
