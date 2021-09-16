cache = {}

def fibo(n, s, e):
    if n == 1:
        return f'{s} {e}\n'
    if (n, s, e) in cache:
        return cache[(n, s, e)]
    t = 6 - s - e
    res = [fibo(n - 1, s, t),
           f'{s} {e}\n',
           fibo(n - 1, t, e)]
    cache[(n, s, e)] = ''.join(res)
    return cache[(n, s, e)]

N = int(input())
print(2 ** N - 1)
print(fibo(N, 1, 3))