from collections import deque
for T in range(int(input())):
    n,k = map(int,input().split())
    node = [[] for _ in range(n+1)]
    csttime = [0] + list(map(int,input().split()))
    cst=[-1 for _ in range(n+1)]
    for _ in range(k):
        p,s = map(int,input().split())
        node[s].append(p)
    d = int(input())
    q = deque([d])
    if node[d] == []:
        sol = csttime[s]
        q.popleft()
    while q:
        s = q.popleft()

        if cst[s]==-1:
            cst[s]= csttime[s]
        for x in node[s]:
            tmp = cst[s] + csttime[x]
            if cst[x]<tmp:
                cst[x] = tmp
                q.append(x)
                sol = tmp
            else:
                pass
    print(sol)

