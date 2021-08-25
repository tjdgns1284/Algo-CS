S = list(input())
a = ord('a')
sol = [-1 for _ in range(26)]
for idx, s in enumerate(S):
    if a+26>=ord(s)>=a:
        x = ord(s)-a
        if sol[x]==-1:
            sol[x] = idx

for i in sol:
    print(i, end=' ')
