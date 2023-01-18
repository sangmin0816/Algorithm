import sys
input = sys.stdin.readline

N, M, K = map(int, input().split(' '))
student = list()
final = list()
ans = 0

for m in range(M):
    participant = list(map(float, input().split(' ')))
    
    while(len(participant)):
        stat = participant.pop()
        num = participant.pop()
        student.append([stat, int(num)])

student.sort(reverse = True)

for s, i in student:
    if i not in final:
        final.append(i)
        ans += s
    if len(final)==K:
        break

print(round(ans, 1))