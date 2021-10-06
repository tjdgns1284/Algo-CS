
import sys
input = sys.stdin.readline
def printer():
    for i in range(9):
        for j in range(9):
            if j != 8:
                print(board[i][j], end=' ')
            else:
                print(board[i][j])
    exit(0)

def check(m):

    if m ==81:
        printer()

    i=m//9
    j=m%9
    if board[i][j] != 0:
        check(m+1)
    gn = [0]+ [1]*9
    sn = [0]+ [1]*9
    qn = [0]+ [1]*9
    for x in range(9):
        if board[i][x]:
            gn[board[i][x]] = 0
        if board[x][j]:
            sn[board[x][j]] = 0
    qi = (i//3)*3
    qj = (j//3)*3

    for x in range(qi,qi+3):
        for y in range(qj,qj+3):
            if board[x][y] :
                qn[board[x][y]] = 0

    for k in range(10):
        if gn[k]==0 or sn[k]==0 or qn[k]==0:
            continue
        else:
            board[i][j] = k
            check(m+1)
            board[i][j] = 0

    else:
        return 0


    return 0



board= [list(map(int,input().split())) for _ in range(9)]
check(0)




