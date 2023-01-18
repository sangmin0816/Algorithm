#https://www.acmicpc.net/problem/2161
N = int(input())
cards = [i+1 for i in range(N)]
for i in range(N-1):
    print(cards.pop(0), end=' ')
    cards.append(cards.pop(0))
print(cards.pop(0))