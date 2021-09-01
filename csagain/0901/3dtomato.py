dr=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
m,n,h= map(int,input().split())
boxes = [list(list(map(int,input().split())) for __ in range(n) ) for _ in range(h)]
stack =[]
for d in range(h):
    for y in range(n):
        for x in range(m):
            if boxes[d][y][x]==1:
                stack.append((d,y,x))

cnt = -1
while stack:
    cnt+=  1
    new_stack=[]
    for a in stack:
        d,y,x = a
        for dir in dr:
            nd = d + dir[0]
            ny = y + dir[1]
            nx = x + dir[2]
            if nd>=h or nd<0 or ny>=n or ny<0 or nx>=m or nx<0:
                continue
            if boxes[nd][ny][nx]==0:
                boxes[nd][ny][nx] = 1
                new_stack.append((nd,ny,nx))
    stack= new_stack.copy()

for d in range(h):
    if cnt==-1:
        break
    for y in range(n):
        if cnt ==-1:
            break
        for x in range(m):
            if boxes[d][y][x]==0:
                cnt = -1
                break
print(cnt)