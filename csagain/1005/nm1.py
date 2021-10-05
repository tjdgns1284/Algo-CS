import copy
n, m = map(int, input().split())
arr = list( i for i in range(1,n+1))
subset=[]
for x in arr:
    subset.append([x])
cnt = 1
while cnt<m:
    n_subset=[]
    for k in subset:
        for i in arr:
            if i not in k:
                nk= k + [i]
                n_subset.append(nk)

    subset = copy.deepcopy(n_subset)
    cnt += 1

subset.sort()
for per in subset:
    for x in per:
        print(x, end=' ')
    print()