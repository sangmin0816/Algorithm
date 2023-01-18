#12873 기념품

N = int(input()) # 사람 수

team = [i+1 for i in range(N)] # 티셔츠에 적힌 수들

fail = 0 # 시작 지점. 탈락자의 티셔츠 수

for i in range(N-1): # 한 명 남을 때까지
    fail = (fail+(i+1)**3)%(N-i) # 남아있는 참가자 원에서 t의 세제곱만큼 돌렸을 때 백준이의 위치
    if(fail==0):
        team.pop(N-i-1) # 남아있는 참가자 중 마지막 사람의 인덱스
    else:
        team.pop(fail-1) # 탈락자의 인덱스
        fail -= 1 # 인원이 줄었으므로, fail도 하나 줄음

print(team[0])