for T in range(int(input())):
    x1,y1,x2,y2= map(int,input().split())
    n= int(input())
    cnt = 0
    for _ in range(n):
        a,b,r = map(int,input().split())
        r = r**2
        d1 = (a-x1)**2+(b-y1)**2
        d2 = (a-x2)**2+(b-y2)**2
        if r>d1 and r>d2:
            pass
        elif r<d1 and r<d2:
            pass
        else:
            cnt+=1
    print(cnt)