import sys
input = sys.stdin.readline

N = int(input())

dictionary = dict()

for i in range(N):
    arri = list(input().rstrip())
    arri.sort()
    if str(arri) not in dictionary:
        dictionary[str(arri)]=0
    dictionary[str(arri)]+=1

print(len(dictionary.keys()))