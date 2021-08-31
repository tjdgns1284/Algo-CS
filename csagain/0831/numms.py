n=int(input())
arr=list(map(int,input().split()))
sol = {}
for x in arr:
    if x in sol:
        sol[x] += 1
    else:
        sol[x] = 1
sol =sorted(sol.items(), key= lambda x:x[0])
last_ssum = 0
real =[]
print(sol)
for y in range(len(sol)):
    y=list(sol[y])

    y[1] =last_ssum
    last_ssum +=1
    real.append(y)
real=dict(real)
for num in arr:
    print(real[num],end=' ')