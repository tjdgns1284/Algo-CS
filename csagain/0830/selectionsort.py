n=int(input())
arr =[]
for _ in range(n):
    arr.append(int(input()))

for i in range(n-1):
    mini = arr[i]
    mini_idx=i
    for j in range(i+1,n):
        if arr[j]<mini:
            mini=arr[j]
            mini_idx=j
    if i != mini_idx:
        arr[i],arr[mini_idx] = arr[mini_idx],arr[i]
for k in range(n):
    print(arr[k])