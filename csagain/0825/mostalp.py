word = list(input())
Ea = [0 for _ in range(26)]
a = ord('a')
A = ord('A')
for alphabet in word:
    x = ord(alphabet)
    if a+26 >= x >= a:
        Ea[x-a] += 1
    else:
        Ea[x-A] += 1
maxv = 0
maxi = 0
ques = 0
for i in range(26):
    if Ea[i]>maxv:
        maxv = Ea[i]
        maxi = i
        ques = 0
    elif Ea[i] == maxv:
        ques = 1
if ques:
    print('?')
else:
    ans = chr(A+maxi)
    print(ans)


