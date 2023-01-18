import sys
input = sys.stdin.readline

sudoku = list()

for i in range(9):
    sudoku.append(list(map(int, list(input().rstrip()))))
    
zeros = list()
for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            zeros.append([i, j])
            
def recur(cnt):
    if cnt==len(zeros):
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end='')
            print()
        
        sys.exit(0)
    
    x, y = zeros[cnt]
    
    for i in range(1, 10):
        if sudoku[x][y]==0 and check(x, y, i):
            sudoku[x][y]=i
            recur(cnt+1)
            sudoku[x][y]=0

def check(x, y, val):
    for i in range(9):
        if i!=y and sudoku[x][i] == val:
            return False
        if i!=x and sudoku[i][y] == val:
            return False
    
    x_range = x//3*3
    y_range = y//3*3
    for i in range(x_range, x_range+3):
        for j in range(y_range, y_range+3):
            if i!=x and j!=y and sudoku[i][j]==val:
                return False
    
    return True
            
recur(0)