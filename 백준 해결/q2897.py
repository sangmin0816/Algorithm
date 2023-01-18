# 말이 브루트포스지 그냥 단순무식 아닐까
import sys
input = sys.stdin.readline

R, C = map(int, input().split(' '))
cars = [input().rstrip() for i in range(R)]
parking = [0, 0, 0, 0, 0]

for i in range(R-1):
    for j in range(C-1):
        temp = (cars[i][j:j+2].count('X') + cars[i][j:j+2].count('#')*10)
        temp += (cars[i+1][j:j+2].count('X') + cars[i+1][j:j+2].count('#')*10)
        if temp<10:
            parking[temp]+=1
        
 
for i in parking:
    print(i)