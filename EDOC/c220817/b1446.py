#1446
import sys
input = sys.stdin.readline

N, D = map(int, input().split(' '))

arr = [[] for i in range(D+1)] # 고속도로

for i in range(N):
    s, e, w = map(int, input().split()) # 시작, 끝, 길이
    if e<=D:
        arr[s].append([w, e])

distance = [i for i in range(D+1)] # 고속도로 없이 그냥 이동
 
for i in range(D+1):
    if i != 0:
        distance[i] = min(distance[i], distance[i-1]+1)
        # 그냥 이동과 고속도로 이용해 온 경우의 값 비교
    for w, e in arr[i]: # 그냥 이동 > 고속도로 이용 값 --> 갱신
        if distance[e] > w + distance[i]: 
            distance[e] = w + distance[i]
 
print(distance[D]) # 도착지까지 최소 비용