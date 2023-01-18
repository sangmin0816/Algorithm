import sys
input = sys.stdin.readline

X = float(input())
flag = 0
max = 10**8
answer = []

for i in range(1000):
    if(i*X != int(i*X)):
        continue
    else:
        if(int(i*X%10) == int(str(i)[0])):
            if(str(int(i*X/10)) == str(i)[1:]):
                answer.append(i)

if(not len(answer)):
    print("No solution")
else:
    for i in answer:
        for j in range(2, 8):
            if(len(str(i)*j) > 8):
                break
            answer.append(int(str(i)*j))
    answer.sort()
    for i in answer:
        print(i)