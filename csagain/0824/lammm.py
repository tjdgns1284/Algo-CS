arr = []
cnt = 0
for i in range(10):
    x = int(input())%42
    if x not in arr:
        arr.append(x)
        cnt += 1
print(cnt)