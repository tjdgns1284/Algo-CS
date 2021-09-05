from collections import  deque
dr = [(1,0),(-1,0),(0,1),(0,-1)]
n,m=map(int,input().split())

arr = [list(input()) for _ in range(n)]
visit = [list(list(-1 for _ in range(2)) for _ in range(m)) for _ in range(n)]
visit[0][0][1] = 1
queue=deque()
queue.append((0,0,1))
while queue:
    a = queue.popleft()
    i,j,b = a
    if i==n-1 and j==m-1:
        break
    if b:
        k = visit[i][j][1]
    else:
        k = visit[i][j][0]
    for x in range(4):
        ni = i + dr[x][0]
        nj = j + dr[x][1]
        if ni>=n or nj>=m or ni<0 or nj<0:
            continue
        if arr[ni][nj]=='0' and visit[ni][nj][b] == -1:
            visit[ni][nj][b] = k+1
            queue.append((ni,nj,b))
        elif arr[ni][nj]=='1' and b:
            visit[ni][nj][0] = k+1
            queue.append((ni, nj, 0))

if visit[n-1][m-1][0] ==-1 and visit[n-1][m-1][1]==-1:
    print(-1)
elif visit[n-1][m-1][0] ==-1:
    print(visit[n-1][m-1][1])
else:
    print(visit[n-1][m-1][0])