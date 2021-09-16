p = [0 for _ in range(123456*2+1)]
for x in range(2,123456*2+1):
    z= int(x**(1/2))+1
    for k in range(2,z):
        if x%k==0:
            break
    else:
        p[x]=1

while True:
    n=int(input())
    if n==0:
        break
    cnt =0
    for i in range(n+1,2*n+1):
        if p[i]:
            cnt +=1

    print(cnt)