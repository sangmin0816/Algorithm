import sys
input = sys.stdin.readline

N = int(input())
global ans
ans = 0

def recur(cnt, queen):
    global ans
    if cnt == N:
        ans += 1
        return
    for i in range(N):
        flag = True
        for j in range(cnt):
            if i==queen[j] or abs(i-queen[j]) == cnt - j:
                flag = False
                break
        if flag:
            queen[cnt] = i
            recur(cnt+1, queen)
            
recur(0, [False for n in range(N)])
print(ans)