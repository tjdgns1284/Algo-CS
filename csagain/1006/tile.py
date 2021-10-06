
n=int(input())
a,b=1,2
if n==1 :
    print(1)
if n==2:
    print(2)
if n>2:
    for _ in range(n-2):
        a,b= b%15746, (a+b)%15746
    print(b)



