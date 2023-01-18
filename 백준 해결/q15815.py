# 피연산자 찾기가 중요!

import sys
input = sys.stdin.readline

S = input().rstrip()
operator = ['+', '-', '*', '/']

temp = []
for s in S:
    if s not in operator:
        temp.append(int(s))
    else:
        operand2 = temp.pop()
        operand1 = temp.pop()
        if s == '+':
            temp.append(operand1+operand2)
        elif s == '-':
            temp.append(operand1-operand2)
        elif s == '*':
            temp.append(operand1*operand2)
        elif s == '/':
            temp.append(operand1//operand2)

print(temp.pop())