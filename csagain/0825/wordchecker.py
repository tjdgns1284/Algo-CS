n = int(input())
ssum = 0
x = ord('a')
for i in range(n):
    a = input()
    alp = [0 for _ in range(26)]
    last = ''
    for k in a:
        c = ord(k)-x
        if alp[c]==1:
            if k==last:
                continue
            else:
                break
        else:
            alp[c] = 1
            last = k
    else:
        ssum += 1
print(ssum)