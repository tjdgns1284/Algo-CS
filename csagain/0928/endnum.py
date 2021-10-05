

arr = []
pt = 666
while len(arr)<10002:
    x = str(pt)
    if '666' in x:
        arr.append(pt)
    pt+=1

n=int(input())
print(arr[n-1])


