n,x = map(int,input().split())
arr =list(map(int,input().split()))
min_c = 1<<32
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            ss= arr[i]+arr[j]+arr[k]
            c = x-ss
            if c<0:
                continue
            if c<min_c:
                min_c=c
print(x-min_c)