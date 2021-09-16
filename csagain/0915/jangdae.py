def hanoi(N,a,b):
    if N == 1:
        return [[a,b]]
    return hanoi(N-1,a,6-a-b)+[[a,b]]+hanoi(N-1,6-a-b,b)

N = int(input())

print(2**N-1)
x = hanoi(N,1,3)
for i in range(len(x)):
    print(x[i][0],x[i][1])