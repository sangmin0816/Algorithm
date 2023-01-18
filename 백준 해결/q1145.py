# 좀 더 똑똑한 방법으로 풀 수는 없을까
import sys
input = sys.stdin.readline

arr = list(map(int, input().split(' ')))
arr.sort()

ans = arr[2]

while(True):
    flag = 0
    for i in arr:
        if ans%i == 0:
            flag += 1
        
    if flag>2:
        print(ans)
        sys.exit(0)
    
    ans+=1