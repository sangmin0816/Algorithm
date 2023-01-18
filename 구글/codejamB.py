import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    

    printers = [[] for i in range(4)]
    for p in range(3):
        C, M, Y, K = map(int, input().split(' '))
        printers[0].append(C)
        printers[1].append(M)
        printers[2].append(Y)
        printers[3].append(K)
    
    ans = []

    for c in range(4):
        ans.append(min(printers[c]))

    if sum(ans) < 1000000:
        ans = ["IMPOSSIBLE"]
    elif sum(ans) > 1000000:
        remain = sum(ans)-1000000
        if remain>sum(ans):
            ans = ["IMPOSSIBLE"]
            break
        for i in range(len(ans)):
            if ans[i]>remain:
                ans[i]-=remain
                remain = 0
            else:
                remain = remain-ans[i]
                ans[i] = 0
            if remain==0:
                break

    print('Case #%d: ' %(t+1), end='') #띄어쓰기 안 해서 틀림 ㅋㅋㅋㅋ
    for a in ans:
        print(a, end=' ')
    print()