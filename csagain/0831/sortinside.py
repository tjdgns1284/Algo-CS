n=int(input())
arr = [0 for _ in range(10)]
while n:
    x = n%10
    n //= 10
    arr[x] += 1
ans =''
for i in range(9,-1,-1):
    ans += str(i)*arr[i]
print(ans)
