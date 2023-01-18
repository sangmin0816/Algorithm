import sys
input = sys.stdin.readline

N = int(input())
apartement = list(list(map(int, input().rstrip())) for i in range(N))

num = []

row = [1, -1, 0, 0]
col = [0, 0, 1, -1]

def dfs(i, j):
    if i<0 or i>=N or j<0 or j>=N:
        return False 
    if apartement[i][j]==1:
        apartement[i][j]=0
        global cnt
        cnt += 1
        for v in range(4):
            dfs(i+row[v], j+col[v])
        return True
    return False

cnt = 0

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            num.append(cnt)
            cnt = 0
                
print(len(num))
num.sort()
for n in num:
    print(n)