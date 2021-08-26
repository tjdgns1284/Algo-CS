a,b = map(str,input().split())
a = list(a)
b = list(b)
n = len(a)
m = len(b)
sol = []
c = 0
if n>m:
    b=['0' for _ in range(n-m)] + b
    m=n
else:
    a = ['0' for _ in range(m-n)] +a
    n=m
for i in range(n):
    k = int(a[n-1-i])+int(b[m-1-i])+c
    if k>=10:
        c = 1
        k -= 10
        sol.append(str(k))
    else:
        c = 0
        sol.append(str(k))
if c:
    sol.append('1')
sol.reverse()
ans = ''.join(sol)
print(int(ans))