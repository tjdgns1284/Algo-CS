mem= [0] * 8421
def w(a,b,c):
    x = a*400 + b*20 + c
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    if mem[x]:
        return mem[x]
    if a<b and b<c :
        r = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        mem[x] = r
        return r
    else:
        r = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        mem[x] = r
        return r

while True:
    a,b,c = map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    r = w(a, b, c)
    print(f'w({a}, {b}, {c}) = {r}')
