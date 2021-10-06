def rec(x):
    global n
    if len(x)==n:
        cand.append(x)
        return

    for i in range(1,n+1):
        if i in x:
            continue
        k = len(x)
        s=0
        for j in range(1,k+1):

            if x[k-j] == i-j or x[k-j]==i+j:
                s=1
                break
        if s:
            continue
        rec(x+[i])

n=int(input())
cand = []
rec([])

print(len(cand))
