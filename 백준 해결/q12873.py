#https://www.acmicpc.net/problem/12873
N = int(input())
team = [i+1 for i in range(N)]
fail = 0
for i in range(N-1):
    fail = (fail+(i+1)**3)%(N-i)
    if(fail==0):
        team.pop(N-i-1)
    else:
        team.pop(fail-1)
        fail -= 1
print(team[0])