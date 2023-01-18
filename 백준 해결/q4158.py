#https://www.acmicpc.net/problem/4158
#sys.stdin.readline() 이거 쓰는 법 항상 잊지 말기. 으렵다 증말
import sys

while(True):
    N, M = map(int, sys.stdin.readline().strip().split(' '))
    if(N==0 and M==0): break
    duplication = set()
    
    for i in range(N):
        duplication.add(int(sys.stdin.readline()))
        
    for i in range(M):
        duplication.add(int(sys.stdin.readline()))
        
    ans = N + M - len(duplication)
    print(ans)