import sys
input = sys.stdin.readline

N = int(input())

meeting = list()
for n in range(N):
    start, end = map(int, input().split(' '))
    meeting.append([start, end])

meeting.sort(key=lambda x:(x[1], x[0]))

pe = 0
ans = 0
for s, e in meeting:
    if pe <= s:
        ans += 1
        pe = e

print(ans)