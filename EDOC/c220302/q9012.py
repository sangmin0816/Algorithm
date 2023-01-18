import sys
input = sys.stdin.readline

T = int(input())
inputs = [input().rstrip() for _ in range(T)]


def solution(T, inputs):
	answer = []
	for i in range(T):
		temp = []
		for j in inputs[i]:
			if(j=='('):
				temp.append(j)
			else:
				if(not len(temp)):
					temp.append("NO")
					break
				temp.pop()
		if(not len(temp)):
			answer.append("YES")
		else:
			answer.append("NO")
	
	return answer

answer = solution(T, inputs)

for i in answer:
    print(i)