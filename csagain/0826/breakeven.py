a,b,c = map(int,input().split())

p = c-b
if p<=0:
    print(-1)
else:
    x = a//p
    if x*p -a>0:
        print(x)

    else:
        print(x+1)