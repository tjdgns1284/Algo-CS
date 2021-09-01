from collections import  deque
dr = [(1,0),(-1,0),(0,1),(0,-1)]
n,m=map(int,input().split())

arr = [list(input()) for _ in range(n)]
visit = [list(-1 for _ in range(m)) for _ in range(n)]
visit[0][0] = 1
queue=deque()
queue.append((0,0,1))
while queue:
    a = queue.popleft()
    i, j, breakable = a
    k = visit[i][j]
    for x in range(4):
        ni = i +dr[x][0]
        nj = j +dr[x][1]
        if ni>=n or nj>= m or ni<0 or nj<0:
            continue
        if visit[ni][nj]==-1 or visit[ni][nj]>k+1:
            if arr[ni][nj]=='0':
                visit[ni][nj] = k+1
                queue.append((ni,nj,breakable))
            else:
                if breakable:
                    visit[ni][nj] = k+1
                    queue.append((ni, nj, 0))
        if visit[ni][nj]==k+1 and breakable:
            if arr[ni][nj]=='0':
                visit[ni][nj] = k+1
                queue.append((ni,nj,breakable))
print(visit[n-1][m-1])