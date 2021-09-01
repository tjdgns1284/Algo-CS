def dfs(y,x,n,m):
    stack = [(y,x)]
    while stack:
        a = stack.pop()
        y = a[0]
        x = a[1]
        farm[y][x]=0
        for d in dr:
            ny = y + d[0]
            nx = x + d[1]
            if ny>=n or nx>=m or ny<0 or nx<0:
                continue
            if farm[ny][nx]==1:
                stack.append((ny,nx))
    return


dr = [(1,0),(-1,0),(0,1),(0,-1)]
for case in range(int(input())):
    m,n,k= map(int,input().split())
    farm = [list(0 for _ in range(m)) for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        farm[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if farm[i][j]==1:
                cnt += 1
                dfs(i,j,n,m)
    print(cnt)