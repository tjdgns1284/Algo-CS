dr = [(1,0), (-1,0), (0,1), (0,-1)]
def dfs(i,j,n):
    stack=[(i,j)]
    visited=[(i,j)]
    cnt = 0
    while stack:
        now = stack.pop()
        cnt +=1
        loc[now[0]][now[1]]='0'
        for x in range(4):
            ni = now[0] +dr[x][0]
            nj = now[1] +dr[x][1]
            if ni>=n or ni<0 or nj>=n or nj<0:
                continue
            else:
                if loc[ni][nj]=='1' and (ni,nj) not in visited:
                    stack.append((ni,nj))
                    visited.append((ni, nj))

    return cnt
n=int(input())
loc = [list(input()) for _ in range(n)]
count = 0
apart=[]
for i in range(n):
    for j in range(n):
        if loc[i][j]=='1':
            count += 1
            x = dfs(i,j,n)
            apart.append(x)
apart.sort()
print(count)
for k in apart:
    print(k)