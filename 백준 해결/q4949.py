# 백 트래킹 안 넣었다고, 시간초과도 아니고 틀림 처리라니 너무하네
# https://www.acmicpc.net/problem/4949

import sys
input = sys.stdin.readline

while(True):
    str = input()
    if str == '.\n' or str == '.':
        break

    temp = []
    flag = True

    for i in str:
        if (i=='(') or (i=='['):
            temp.append(i)
        elif (i==')') or (i==']'):
            flag = False
            if len(temp):
                popped = temp.pop()
                if (popped == '(') and (i==')'):
                    flag = True
                elif (popped == '[') and (i==']'):
                    flag = True
                else:
                    break
            if not flag: # 이거 하나 안 넣었다고 틀렸다고 한다. 시간초과도 아니라 엄청 헤맸다.
                break # 백트래킹 안 넣으면 틀리게 하는 경우도 있나보다.
    
    if len(temp):
        flag = False

    if(flag):
        print("yes")
    else:
        print("no")