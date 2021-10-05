n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
arr2 = [0 for _ in range(n)]

for i in range(n):
    cnt =0
    for j in range(n):
        if i==j:
            cnt +=1
            continue
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            cnt +=1
    arr2[i]=cnt

for x in arr2:
    print(x,end=' ')
