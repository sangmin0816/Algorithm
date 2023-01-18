# 머지 왜 이게 맞은거지? 뭐 맞았다니깐 그냥 넘어가야지...
# https://www.acmicpc.net/problem/2061 좋은 암호
import sys
input = sys.stdin.readline

K, L = map(int, input().split(' '))

for i in range(2, L):
    if(K%i==0):
        print("BAD", i)
        sys.exit(0)

print("GOOD")