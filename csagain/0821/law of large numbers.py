n,m,k = map(int,input().split())
arr = list(map(int,input().split()))

first = -1<<32
second = -1<<32
for num in arr:
    if num > first:
        second = first
        first = num
    elif num>second:
        second = num

ssum = 0
while m != 0:
    if m >= k:
        ssum += k*first
        m -= k
        if m:
            ssum += second
            m -= 1
    else:
        ssum += m*first
        m = 0

print(ssum)



