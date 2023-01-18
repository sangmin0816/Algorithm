# 맞는 건 적어도 이해라도 가지, 틀리는 건 상상도 못한 이유로 틀린다

import sys
input = sys.stdin.readline

arr = list(map(int, input().split(' ')))
n = int(input())

arr.sort()
ans = set()

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if (arr[i]+arr[j]) == n:
            ans.add(str(arr[i])+" "+str(arr[j]))
        elif arr[i]+arr[j] > n:
            break

ans = list(ans)
ans.sort()
for i in ans:
    print(i)

print(len(ans))