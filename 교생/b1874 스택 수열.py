import sys
input = sys.stdin.readline

N = int(input())
arr = list()

for n in range(N):
    arr.append(int(input()))

number = [i for i in range(N, 0, -1)]
stack = [0]
now = 0

ans = list()

for a in arr:
    while stack[-1]<a:
        if number:
            stack.append(number.pop())
            ans.append('+')
        else:
            print("NO")
            sys.exit(0)
    if stack[-1]!=a:
        print("NO")
        sys.exit(0)
    stack.pop()
    ans.append('-')

for a in ans:
    print(a)