# https://www.acmicpc.net/problem/1935
import sys
input = sys.stdin.readline

N = int(input())
expression = input().rstrip()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
variable = dict()

for i in range(N):
    variable[alphabet[i]] = int(input())

temp = list()
operator = ['+', '-', '*', '/']
for i in expression:
    if i not in operator:
        temp.append(variable[i])
    else:
        operand1 = temp.pop()
        operand2 = temp.pop()
        if i == '+':
            temp.append(operand2+operand1)
        elif i == '-':
            temp.append(operand2-operand1)
        elif i == '*':
            temp.append(operand2*operand1)
        elif i == '/':
            temp.append(operand2/operand1)

print('%.2f' %(temp.pop()))