from collections import  deque


cords = [0 for _ in range(100001)]
a,b = map(int,input().split())
queue=deque()
queue.append(a)
cords[b]=999999
cords[a] =0
while queue:
    now = queue.popleft()
    x = cords[now]
    if x >= cords[b]:
        continue
    n1= now+1
    n2= now-1
    n3= now*2
    if n1<100001 and (cords[n1]==0 or cords[n1]>x+1):
        cords[n1] = x+1
        queue.append(n1)
    if n2>=0 and (cords[n2]==0 or cords[n2]>x+1):
        cords[n2] = x+1
        queue.append(n2)
    if n3 < 100001 and (cords[n3] == 0 or cords[n3] > x + 1):
        cords[n3] = x + 1
        queue.append(n3)
print(cords[b])


