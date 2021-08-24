a=int(input())
b=int(input())
c=int(input())
n = a*b*c
n = str(n)
arr = [0 for _ in range(10)]
for x in n:
    arr[int(x)] += 1
for k in arr:
    print(k)