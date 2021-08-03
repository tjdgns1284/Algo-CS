n = int(input())
for _ in range(n):
    x1,y1,r1,x2,y2,r2= map(int,input().split())
    r3sq = (x1-x2)**2 +(y1-y2)**2
    r3 = r3sq**(1/2)

    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
        else:
            print(0)
    elif abs(r1-r2)<r3< r1+r2:
        print(2)
    elif r3+r1 == r2:
        print(1)
    elif r3+r2 == r1:
        print(1)
    elif r3 ==r1+r2:
        print(1)

    else:
        print(0)


