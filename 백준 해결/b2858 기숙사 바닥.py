import sys
input = sys.stdin.readline

R, B = map(int, input().split(' '))

area = R+B
divisor = list()

for i in range(2, int(area**(1/2))+1):
    if area%i==0:
        divisor.append([area//i, i])
        
for L, W in divisor:
    if ((L+W)*2-4) == R:
        print(L, W)
        break