a,b,v = map(int,input().split())
k = v-a
n = k//(a-b)
if k%(b-a):
    n += 1
print(n+1)