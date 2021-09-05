from collections import deque

moving = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]


for case in range(int(input())):
    n = int(input())
    si,sj = map(int,input().split())
    ei,ej = map(int,input().split())
    visit = [list(-1 for _ in range(n)) for _ in range(n)]
    queue= deque()
    visit[si][sj] =0
    queue.append((si,sj))
    ans = 0
    while queue:
        a = queue.popleft()
        i,j = a
        k = visit[i][j]
        if i == ei and j == ej:
            ans = k
            break
        for x in range(8):
            ni = i + moving[x][0]
            nj = j + moving[x][1]
            if ni>=n or nj>=n or ni<0 or nj<0:
                continue
            if visit[ni][nj]==-1:
                visit[ni][nj]=k+1
                queue.append((ni,nj))
    print(ans)