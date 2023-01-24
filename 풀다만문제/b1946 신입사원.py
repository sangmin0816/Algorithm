import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    applicants = list()
    ans = 1
    
    for n in range(N):
        resume, interview = map(int, input().split(' '))
        applicants.append([resume, interview])
    
    applicants.sort(key=lambda x:x[0])
    resume_1st = applicants[0]
    applicants.sort(key=lambda x:x[1])
    interview_1st = applicants[0]
    
    if resume_1st != interview_1st:
        ans += 1
        temp = list()
        for r, i in applicants:
            if r<interview_1st[0] and i<resume_1st[1]:
                temp.append([r, i])
        
        if temp:
            temp.sort(key=lambda x:x[0])
            resume_2nd = temp[0]
            temp.sort(key=lambda x:x[1])
            interview_2nd = temp[0]
            if resume_2nd!=interview_2nd:
                ans+=1
            ans+=1
    
    print(ans)