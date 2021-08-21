n=int(input())
parlist=[[] for _ in range(n)]
index = []
for i in range(n):
    n = int(input())
    if i:
        parlist[i] = parlist[(i-1)//2].copy()
        parlist[i].append(n)
    else:
        parlist[i].append(n)
    index.append(n)
begint=int(input())
endt=int(input())
for i in range(len(index)):
    if index[i] == begint:
        begin = i
    elif index[i] == endt:
        end = i
i = 0
sol = 0
while True:
    if endt in parlist[begin] and begint not in parlist[end]:
        sol = endt
        break
    elif begint in parlist[end] and endt not in parlist[begin]:
        sol = begint
        break
    if i>=len(parlist[begin]) or i>=len(parlist[end]):
        break
    if parlist[begin][i] == parlist[end][i]:

        sol = parlist[begin][i]
        i += 1
    else:
        break
print(sol)