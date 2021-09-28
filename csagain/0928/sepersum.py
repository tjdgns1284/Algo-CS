def func(n):
    m = str(n)
    x = len(m)
    l = n-9*x
    for ss in range(l,n):
        if ss<0:
            continue
        ss2=str(ss)
        ss3=ss
        for x in ss2:
            ss3+=int(x)
        if ss3 ==n:
            return  ss

    else:
        return 0


n=int(input())
ans = func(n)
print(ans)