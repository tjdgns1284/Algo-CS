minn, maxx = map(int,input().split())
i=2
sol = [0 for _ in range(maxx-minn+1)]
while (i**2)<=maxx:
    y = i**2
    ma = minn//y
    if minn%y!=0:
        ma += 1
    while y*ma<= maxx:
        sol[y*ma-minn]=1
        ma += 1
    i += 1
c = 0
for x in sol:
    if x==0:
        c+=1
print(c)