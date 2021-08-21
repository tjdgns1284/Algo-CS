fibon=[[1,0],[0,1],[1,1]]

def fibo(n):

    if n<len(fibon):
        return 0
    elif n==len(fibon):
        fibon.append([fibon[n-1][0]+fibon[n-2][0],fibon[n-1][1]+fibon[n-2][1]])
    else:
        while n>len(fibon):
            fibo(len(fibon))
        fibon.append([fibon[n-1][0]+fibon[n-2][0],fibon[n-1][1]+fibon[n-2][1]])
    return 0


n = int(input())
for _ in range(n):
    x = int(input())
    fibo(x)
    print(fibon[x][0],fibon[x][1])