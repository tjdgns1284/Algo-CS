n= int(input())
i = 1
while True:
    x = (i**2+i)//2
    if n<=x:
        break
    i += 1
g = n-((i-1)**2+(i-1))//2 -1
if i%2:
    a = i - g
    b = 1 + g
else:
    a = 1 + g
    b = i - g

print(f'{a}/{b}')