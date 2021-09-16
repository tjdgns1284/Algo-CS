import sys
p=[ 0 for _ in range(10001) ]
for x in range(2,10001):
    z= int(x**(1/2))+1
    for k in range(2,z):
        if x%k==0:
            break
    else:
        p[x]=1


for T in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    z= n//2
    for k in range(z,1,-1):

        if p[k] and p[n-k]:
            ans1, ans2 = k,n-k
            break
    print(ans1,ans2)