#https://www.acmicpc.net/problem/1158
N, K = map(int, input().split(' '))
array = [i+1 for i in range(N)]
print("<", end='')

index = 0
for i in range(N-1):
    index = (index+K)%(N-i)
    if(index==0): index=N-i-1
    else: index-=1
    print(array.pop(index), end=', ')
print(array[0], end='')
print(">", end='')
