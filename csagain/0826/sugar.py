n = int(input())
i = 0
n += 3
while n>0:
    n -= 3
    if n%5==0:
        j= n//5
        print(i + j)
        break
    i += 1
if n<0:
    print(-1)
