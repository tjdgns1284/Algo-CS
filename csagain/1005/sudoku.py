from  collections import deque
import sys
input = sys.stdin.readline


def check(i,j):
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
    cnt = 0
    for k in range(10):
        if gn[k]==0 or sn[k]==0 or qn[k]==0:
            continue
        else:
            board[i][j] = k
            return 1
    return 0



board= [list(map(int,input().split())) for _ in range(9)]

after=deque()
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            r = check(i, j)
            if r:
                continue
            else:
                after.append((i, j))
while after:
    i, j = after.popleft()
    r = check(i, j)
    if r:
        continue
    else:
        after.append((i,j))

for i in range(9):
    for j in range(9):
        print(board[i][j], end=' ')
    print()



