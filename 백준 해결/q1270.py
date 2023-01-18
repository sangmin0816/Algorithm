import sys
input = sys.stdin.readline

N = int(input())

for n in range(N):
    Tarr = list(map(int, input().rstrip().split(' ')))
    T = Tarr.pop(0)
    Tdict = dict()
    ans = "SYJKGW"

    for t in Tarr:
        if not t in Tdict:
            Tdict[t] = 0
        Tdict[t] += 1
    for t in Tdict.keys():
        if Tdict[t]>T//2:
            ans = t
            break
    print(ans)
            