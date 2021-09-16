x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

if x1==x2:
    ans1=x3
elif x1==x3:
    ans1=x2
else:
    ans1=x1


if y1==y2:
    ans2=y3
elif y1==y3:
    ans2=y2
else:
    ans2=y1
print(ans1,ans2)