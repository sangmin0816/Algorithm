import sys
input = sys.stdin.readline

N = int(input())

alphabet = dict()
for n in range(N):
    temp = list(input().rstrip())
    for i in range(len(temp)):
        if temp[i] not in alphabet:
            alphabet[temp[i]] = 0
        alphabet[temp[i]] += 10**(len(temp)-i-1)

numbers = list(alphabet.values())
numbers.sort()

ans = 0

i = 9
while numbers:
    ans+=numbers.pop()*i
    i-=1

print(ans)