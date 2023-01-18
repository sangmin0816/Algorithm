#https://www.acmicpc.net/problem/11507

import sys
input = sys.stdin.readline

cards = input().rstrip()
card_lst = [cards[i:i+3] for i in range(0, len(cards), 3)]
card_dict = {'P':0, 'K':0, 'H':0, 'T':0}

for i in card_lst:
    if i in card_dict:
        print("GRESKA")
        sys.exit(0)
    card_dict[i] = 1
    card_dict[i[0]] += 1

print(13 - card_dict['P'], end = ' ')
print(13 - card_dict['K'], end = ' ')
print(13 - card_dict['H'], end = ' ')
print(13 - card_dict['T'], end = ' ')