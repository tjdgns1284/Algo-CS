
m,n=map(int,input().split())

for x in range(m,n+1):
    if x==1:
        continue
    sosu = 1
    z = int(x**(1/2))+1
    for k in range(2,z):
        if x%k==0:
            sosu=0
            break
    if sosu:
        print(x)
