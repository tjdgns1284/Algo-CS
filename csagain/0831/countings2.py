n= int(input())
arr = [0 for _ in range(8001)]
ssum = 0
for _ in range(n):
    x = int(input())
    ssum +=  x
    arr[x+4000] += 1
k=n//2+1
cand = [] #최빈값후보
max_v = 0
st = 10000
ed = 10000
for i in range(8001):
    if arr[i] and k>0:
        if k > arr[i]:
            k -= arr[i]
        else:
            mid = i-4000
            k = 0
    if arr[i] and st == 10000:
        st = i-4000
    if arr[8000-i] and ed == 10000:
        ed = 4000-i
    if arr[i]>max_v:
        cand = [i-4000]
        max_v = arr[i]
    elif arr[i] == max_v:
        cand.append(i-4000)
avg = round(ssum/n)
if len(cand)>=2:
    freq=cand[1]
else:
    freq=cand[0]
print(avg)
print(mid)
print(freq)
print(ed-st)
