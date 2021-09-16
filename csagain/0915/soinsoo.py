n = int(input())
k = 2
while True:
    if n==1:
        break
    if n%k==0:
        n=n//k
        print(k)
    else:
        k += 1


