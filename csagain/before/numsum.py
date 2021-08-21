N,L = map(int,input().split())
sumtemp = 0
ans = []
while L<=100:
    a=N//L
    x=(L-1)//2
    k=(L-1)%2
    if a-x ==0:
        ans = -1
        break
    if a-x ==1 and k==1:
        if a*(1+2*x) +(a-x-1)== N:
            ans = [(a-x-1 +i ) for i in range(L)]
            break
        else:
            continue

    if k==0:
        sumtemp = a*(1+2*x)
        if sumtemp == N:
            ans = [(a - x + i) for i in range(L)]
            break
    else:
        sumtemp = a*(1+2*x) +(a-x-1)
        if sumtemp == N:
            ans = [(a-x-1 +i ) for i in range(L)]
            break
        sumtemp = a*(1+2*x) +(a+x+1)
        if sumtemp == N:
            ans = [(a + x + 1 - i) for i in range(L)]
            ans.reverse()
            break

    L += 1
    if L ==101:
        ans = -1
        break
print(ans)
