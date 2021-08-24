a,b= map(int,input().split())

time = a*60 + b -45
if time<0:
    time = 24*60 +time
if time >= 24*60:
    time -= 24*60
x = time//60
y = time%60
print(f'{x} {y}')
