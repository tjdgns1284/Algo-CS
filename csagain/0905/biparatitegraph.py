
def dfs(n):
    c=[1]+([0]*n)
    visit = [0 for _ in range(n+1)]
    stack =[]
    for i in range(1,len(c)):
        stack.append(i)
    while stack:
        now = stack.pop()
        if visit[now]:
            continue
        else:
            a= c[now]
            if a ==0:
                a = 1
            visit[now] =1
        for next in arr[now]:
            if c[next]==a:
                return 'NO'
            if a==1 and c[next]==0:
                c[next] = 2
                stack.append(next)
            if a == 2 and c[next] == 0:
                c[next] = 1
                stack.append(next)


    return 'YES'

for case in range(int(input())):
    v,e = map(int,input().split())
    arr = [1]+list([] for _ in range(v))
    for _ in range(e):
        n1,n2 = map(int,input().split())
        arr[n1].append(n2)
        arr[n2].append(n1)
    ans = dfs(v)
    print(ans)
