import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

auto = dict()

for i in range(N):
    site, pwd = map(str, input().split(' '))
    if site not in auto:
        auto[site.rstrip()] = pwd.rstrip()

for i in range(M):
    site = input().rstrip()
    print(auto[site])