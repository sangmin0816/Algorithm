import sys
input = sys.stdin.readline

mushroom = [int(input()) for i in range(10)]
ans = 0

for i in mushroom:
    if abs(100-ans) >= abs(100-ans-i):
        ans += i
    else:
        break

print(ans)