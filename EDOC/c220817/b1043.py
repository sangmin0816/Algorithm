# 1043 거짓말
# 틀림 ^_^
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
T = list(map(int, input().split(' ')))
T = set(T[1:])

participant = []
for m in range(M):
    participant.append(set(list(map(int, input().split(' ')))[1:]))

for m in range(M):
    if T & participant[m]: # 진실을 아는 사람과 파티에 참석한 사람
        T = T.union(participant[m])
        for k in range(m):
            if T&participant[k]:
                T = T.union(participant[k])

ans = 0
for m in range(M): # 진실을 아는 사람과 파티에 한 번도 참석하지 않은 사람
    if T & participant[m]:
        T = T.union(participant[m])
    else:
        ans+=1

print(ans)