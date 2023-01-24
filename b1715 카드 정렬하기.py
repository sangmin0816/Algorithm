import sys
input = sys.stdin.readline

N = int(input())
cards = list()

for n in range(N):
    cards.append(int(input()))

ans = list()

if len(cards)==1:
    ans.append(cards.pop())

while len(cards)>1:
    cards.sort(reverse=True)
    card_1 = cards.pop()
    card_2 = cards.pop()
    cards.append(card_1+card_2)
    ans.append(card_1+card_2)

print(sum(ans))