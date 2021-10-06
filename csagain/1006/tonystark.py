def team(x):
    global n
    if len(x)==n//2:
        pers.append(x.copy())
        return
    for i in range(1,n+1):
        if x and  i <= x[-1]:
            continue
        x.append(i)
        team(x)
        x.pop()
def sumper(lis):
    summm = 0
    for i in range(len(lis)-1):
        for j in range(i+1,len(lis)):
            summm += arr[lis[i]-1][lis[j]-1] + arr[lis[j]-1][lis[i]-1]
    return summm
n= int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

nums= [i for i in range(1,n+1)]
pers=[]
team([])
min_dif = 1<<32
for per in pers:
    notper=[]
    for num in nums:
        if num not in per:
            notper.append(num)
    r1 = sumper(per)
    r2 = sumper(notper)
    res =abs(r1-r2)
    if res ==0:
        min_dif=0
        break
    if res<min_dif:
        min_dif=res
print(min_dif)