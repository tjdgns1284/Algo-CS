import  sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque
def merge(la,ra):
    result = deque()
    la = deque(la)
    ra = deque(ra)
    while len(la)>0 or len(ra)>0:
        if len(la)>0 and len(ra)>0:
            if la[0]>=ra[0]:
                result.append(ra[0])
                ra.popleft()
            else:
                result.append(la[0])
                la.popleft()
        elif len(la)>0:
            result.append(la[0])
            la.popleft()
        elif len(ra)>0:
            result.append(ra[0])
            ra.popleft()
    return  result

def divide(arr):
    if len(arr)<=1:
        return  arr
    mid = len(arr)//2
    leftArr = arr[:mid]
    rightArr = arr[mid:]
    leftArr = divide(leftArr)
    rightArr = divide(rightArr)
    return merge(leftArr,rightArr)

n=int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
r = divide(arr)
for x in r:
    print(str(x)+'\n')