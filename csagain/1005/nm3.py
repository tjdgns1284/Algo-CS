def rec(x):
    global n,m
    if len(x)==m:
        print(' '.join(x))
        return

    for i in range(1,n+1):

        rec(x+[str(i)])


n, m = map(int, input().split())

rec([])