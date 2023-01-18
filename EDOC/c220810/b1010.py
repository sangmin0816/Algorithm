import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N, M = map(int, input().split(' '))
    ans = 1
    bridge = 1
    for i in range(M, M-N, -1): # 정확한 insight가 기억 안 남 ㅠㅠ
        ans = (ans*i)//bridge # N개의 다리 별로 i개의 경우의 수를 가짐. 이 중 다리가 교차되는 bridge 개의 경우를 나눠줌
        bridge += 1
    print(ans)