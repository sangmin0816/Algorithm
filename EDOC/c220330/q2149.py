import sys
input = sys.stdin.readline

key = list(input().rstrip())
crypto_temp = list(input().rstrip())

keylen = len(key)
column = len(crypto_temp)//keylen


key_sort = list() # 글자와 글자의 원래 순서 [H, 0]

for i in range(keylen):
    key_sort.append([key[i], i])

key_sort.sort() # 글자를 알파벳 순으로 정렬

order = list() # 정렬된 알파벳의 원래 순서

for i in range(keylen):
    order.append(key_sort[i][1]) # [3, ...] 암호문의 0번째 글자는 원래 3번째 글자

# print("order", order)


cryptogram = [] # 암호문을 이차원 배열로 저장

for i in range(keylen): # (키)행 (컬럼)열로 암호문 정렬. 
    cryptogram.append(crypto_temp[i*column:(i+1)*column])
    # print(crypto_temp[i*column:(i+1)*column])

plain_text = ""


# 한 열이 한 문장이 되므로, 행을 돌면서 열을 정렬
for j in range(column):
    temp = key
    for i in range(keylen):
        temp[order[i]] = cryptogram[i][j] # 암호문의 n번째 글자는 원래 order[n]번째 글자. ex. 'E' 0번째 글자는 원래 3번째 글자
    plain_text += "".join(temp)

print(plain_text) # 평문 출력