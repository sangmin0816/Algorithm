# https://www.acmicpc.net/problem/2257
import sys
input = sys.stdin.readline

formula = input().rstrip()

temp = list()
flag = False

chemical = {'H': 1, 'C': 12, 'O': 16}
    
for c in formula:
    if c == '(':
        temp.append(c)
    elif c in chemical.keys():
        temp.append(chemical[c])
    elif c == ')':
        sum_temp = 0
        while temp[-1] != '(':
            sum_temp += temp.pop()
        temp.pop()
        temp.append(sum_temp)
    else:
        temp.append(temp.pop()*int(c))

print(sum(temp))