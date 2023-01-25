import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    applicants = list()
    ans = list()
    
    for n in range(N):
        resume, interview = map(int, input().split(' '))
        applicants.append([resume, interview])
     
    applicants.sort(key=lambda x:x[0])
    ans.append(applicants[0])
    
    for r, i in applicants:
        if  ans[-1][1] > i:
            ans.append([r, i])
    
    print(len(ans))