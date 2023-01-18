import sys
input = sys.stdin.readline

N = int(input())

pizza = [0 for i in range(N+3)] #index값 같게하고, i=1일 때도 범위 벗어나지 않도록 0~N+2까지 범위
pizza[2]=1

for i in range(2, N+1):
    if(i%2==0):
        pizza[i] = pizza[i//2]*2 + (i//2)**2
    else:
        pizza[i] = pizza[i//2] + pizza[i//2+1] + (i//2) * (i//2+1)
        # pizaa[5] = pizza[2] + pizza[3] + 2*3(5를 2와 3으로 나눴을 때의 즐거움)

print(pizza[N])



