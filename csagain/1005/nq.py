def rec(x):
    global n
    if len(x)==n:
        cand.append(x)
        return

    for i in range(1,n+1):
        if i in x:
            continue
        rec(x+[i])

n=int(input())
cand = []
rec([])
r=0

print(r)
