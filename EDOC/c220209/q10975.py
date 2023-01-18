N = int(input())

list = []
ans = 0

for i in range(N):
    income = int(input())
    if(len(list)==0): list.append([income])
    elif(list[ans][0]>=income): list[ans].insert(0, income)
    elif(list[ans][len(list[ans])-1]<=income): list[ans].insert(0, income)

print(ans)