def make_k(n,k):
    ans= ''
    while True:
        x= n//k
        y= n%k
        if x == 0:
            ans = str(y) + ans
            break
        ans = str(y) + ans
        n= x
    return ans
def primecheck(n):
    if n ==1:
        return False
    k = int(n**(1/2))
    for c in range(2,k+1):
        if n%c==0:
            return False
    return True

def solution(n, k):
    answer = 0
    x= make_k(n,k)
    arr = list(x.split('0'))
    for c in arr:
        if c:
            c = int(c)
            answer += primecheck(c)

    return answer

print(solution(110011,10))


