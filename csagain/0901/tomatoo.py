dr = [(1,0),(-1,0),(0,1),(0,-1)]
m,n=map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]
stack=[]
for i in range(n):
    for j in range(m):
        if box[i][j]==1:
            stack.append((i,j))
day = -1
while stack:
    new_stack=[]
    day += 1
    for a in stack:
        x = a[0]
        y = a[1]
        for i in range(4):
            nx = x + dr[i][0]
            ny = y + dr[i][1]
            if nx>=n or ny>=m or nx<0 or ny<0:
                continue
            if box[nx][ny]==0:
                box[nx][ny]=1
                new_stack.append((nx,ny))
    stack =new_stack.copy()
for i in range(n):
    if day == -1:
        break
    for j in range(m):
        if box[i][j]==0:
            day=-1
            break
print(day)



