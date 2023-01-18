import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))

countries = dict()
target = ''

for n in range(N):
    name, g, s, c = map(int, input().split(' '))
    temp = tuple([g, s, c])
    if temp not in countries:
        countries[temp] = 0
    countries[temp]+=1
    if name == K:
        target = tuple([g, s, c])

all = 1

for key, value in sorted(countries.items(), reverse=True):
    if key == target:
        print(all)
        break
    all+=value