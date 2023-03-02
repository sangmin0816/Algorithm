import sys
input = sys.stdin.readline

N = int(input())
parents = list(map(int, input().split(' ')))
delete = int(input())

stack = [delete]

while stack:
    now = stack.pop()
    parents[now] = -2

    for i, p in enumerate(parents):
        if p==now:
            parents[i] = -2
            stack.append(i)

ans = 0

for i, p in enumerate(parents):
    if p>=-1 and i not in parents:
        ans+=1

print(ans)