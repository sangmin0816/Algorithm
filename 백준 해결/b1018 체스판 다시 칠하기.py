import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
chess_board = list()

for n in range(N):
    chess_board.append(input().rstrip())

ans = list()

for n in range(N-7):
    for m in range(M-7):
        cnt = 0
        white_board = 0
        black_board = 0
        for i in range(8):
            for j in range(8):
                if (i+j)%2==0:
                    if chess_board[n+i][m+j]=='W':
                        black_board+=1
                    else:
                        white_board+=1
                else:
                    if chess_board[n+i][m+j]=='B':
                        black_board+=1
                    else:
                        white_board+=1
        ans.append(white_board)
        ans.append(black_board)

print(min(ans))

"""
for i in range(0,8,2):
            row = chess_board[n+i][m:m+8]
            white_board += 4-row.count('WB')
            black_board += 4-row.count('BW')
        for i in range(1,8,2):
            row = chess_board[n+i][m:m+8]
            black_board += 4-row.count('WB')
            white_board += 4-row.count('BW')
        ans.append(white_board)
        ans.append(black_board)
"""