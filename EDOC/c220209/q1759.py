L, C = map(int, input().split(' '))
alphlist = list(input().split(' '))

alphlist.sort()

for i in range(L-C+1):
    code = list(alphlist.pop(0))
    temp = alphlist
    while(len(code)==L): code.append(temp.pop(0))