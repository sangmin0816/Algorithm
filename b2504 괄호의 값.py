# 코드가 너무 더러워서 맞아도 맞은 기분이 아니다.

import sys
input = sys.stdin.readline

bracket = list(input().rstrip())
stack = list()
ans = list()

for b in bracket:
    if b=='(':
        stack.append('(')
    elif b=='[':
        stack.append('[')
    else:
        temp = list()
        while True:
            if not stack:
                print(0)
                sys.exit(0)
            now = stack.pop()
            if type(now)==int:
                temp.append(now)
            elif now=='(' and b==')':
                if not temp:
                    temp.append(1)
                stack.append(sum(temp)*2)
                break
            elif now=='[' and b==']':
                if not temp:
                    temp.append(1)
                stack.append(sum(temp)*3)
                break
            else:
                print(0)
                sys.exit(0)

ans = 0
for s in stack:
    if type(s)==int:
        ans+=s
    else:
        print(0)
        sys.exit()

print(ans)
            