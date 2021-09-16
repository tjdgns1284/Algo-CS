n=int(input())
arr=list(map(int,input().split()))
cnt = 0
for x in arr:
    if x==1:
        continue
    sosu = 1
    z = int(x**(1/2))+1
    for k in range(2,z):
        if x%k==0:
            sosu=0
            break
    if sosu:
        cnt +=1
print(cnt)