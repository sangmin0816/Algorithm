import sys
input = sys.stdin.readline

stick = list(input().rstrip())

stack = list()
ans = 0
lazer = False

for s in stick:
    if s=='(':
        stack.append(s)
        lazer = True
    elif stack and lazer:
        stack.pop()
        ans += len(stack)
        lazer = False
    elif stack:
        stack.pop()
        ans += 1

print(ans)