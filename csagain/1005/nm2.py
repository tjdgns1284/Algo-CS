def rec(x):
    global n,m
    if len(x)==m:
        for i in x:
            print(i, end=' ')
        print()
        return

    for i in range(1,n+1):
        if x and  i <= x[-1]:
            continue
        x.append(i)
        rec(x)
        x.pop()







n, m = map(int, input().split())

rec([])