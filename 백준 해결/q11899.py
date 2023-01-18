import sys
input = sys.stdin.readline

S = input().rstrip()

bracket = list()
ans = 0

for i in S:
    if i == '(':
        bracket.append(i)
    else:
        if len(bracket):
            bracket.pop()
        else:
            ans+=1

ans += len(bracket)

print(ans)