def quicks(arr):
    if len(arr)<=1:
        return arr
    less,equal,bigger = [],[],[]
    pivot = arr[len(arr)//2]
    for k in arr:
        if k < pivot:
            less.append(k)
        elif k> pivot:
            bigger.append(k)
        else:
            equal.append(k)
    return quicks(less) + equal + quicks(bigger)

n=int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
ans = quicks(arr)
for k in ans:
    print(k)