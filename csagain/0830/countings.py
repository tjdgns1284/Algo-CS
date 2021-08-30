import sys
input = sys.stdin.readline
print =sys.stdout.write

n=int(input())
tmp =[0 for _ in range(10001)]
for _ in range(n):
   tmp[int(input())] += 1

for k in range(10001):
    if tmp[k]:
        for _ in range(tmp[k]):
            print(str(k)+'\n')
