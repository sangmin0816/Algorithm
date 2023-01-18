import sys
input = sys.stdin.readline

m, n = map(int, input().split(' '))

estate = list()
for i in range(m):
    estate.append(list(map(int, input().split(' '))))

psum = [[0]*302]*302

for i in range(n):
    for j in range(m):
        psum[i][j] = psum[i-1][j]+psum[i][j-1]+estate[i][j]-psum[i-1][j-1]

ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        for k in range(i, n+1):
            for l in range(j, m+1):
                sum = psum[k][l]-psum[i-1]-psum[k][j-1]+psum[i-1][j-1]
                if sum==10:
                    ans+=1
                if sum>=10:
                    break

print(ans)