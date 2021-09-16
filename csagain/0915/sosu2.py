arr= []
m=int(input())
n=int(input())

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
        arr.append(x)
if arr:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)