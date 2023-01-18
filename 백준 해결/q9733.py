# 입력받는 게 제일 어려웠던 문제
# 입력이 없을 때까지 입력받을 때는 readlines를 사용하고 테스트 돌릴 때는 엔터 후 ctrl z를 누르면 된다.
# 파이썬에서 소수점 자릿수를 고정할 때는 "{.f}".format(값) 을 사용한다.
# https://www.acmicpc.net/problem/9733

import sys
input = sys.stdin.readlines # 제한없이 입력받기

workList = {'Re': 0, 'Pt': 0,'Cc': 0,'Ea': 0,'Tb': 0,'Cm': 0, 'Ex': 0, 'Total': 0}

lines = input()

for i in lines:
    worked = list(i.strip().split(' ')) # 뒤에 \n 을 떼주고 리스트로 변환
    for j in worked:
        workList['Total']+=1
        if j in workList.keys():
            workList[j]+=1

for i in workList.keys():
    print(i, workList[i],"{:.2f}".format(workList[i]/workList['Total']))