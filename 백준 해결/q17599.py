import sys
input = sys.stdin.readline

n = int(input())
toxic = dict()

liquid = list(map(int, input().split(' ')))
for i in liquid:
    if i not in toxic:
        toxic[i] = 0
    toxic[i]+=1

print(len(toxic.keys()))