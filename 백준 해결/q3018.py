# 예제는 다 맞는데 왜 틀리는지 모르겠다.
# 곡의 갯수가 문제가 아니라 종류가 문제였다. set를 사용해야 했다.
# https://www.acmicpc.net/problem/3018
# https://burningjeong.tistory.com/317 갯수가 아닌 종류로 구분 알게 된 블로그

import sys
input = sys.stdin.readline

N = int(input())
E = int(input())
participant = dict()
for i in range(N):
    participant[i+1]=[]

for i in range(E):
    campfire = list(map(int, input().split(' ')))
    K = campfire.pop(0)
    flag = False
    noseonyoung = set()

    for j in campfire:
        if j == 1:
            flag = True
            break
        temp = set(participant[j])
        noseonyoung = set.union(noseonyoung, temp)
    
    if(flag):
        for j in campfire:
            participant[j].append(i)
    else:
        for j in campfire:
            participant[j] = list(noseonyoung)

seonyoung = len(participant[1])

for i in sorted(participant.keys()):
    if len(participant[i])==seonyoung:
       print(i)