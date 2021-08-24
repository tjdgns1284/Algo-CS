a = int(input())
b = list(input())
b[0],b[2] = b[2],b[0]
ssum = 0
for idx, x in enumerate(b):
    ssum += (10**idx)*(int(x)*a)
    print(int(x)*a)
print(ssum)
