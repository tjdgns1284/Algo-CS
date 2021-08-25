A = list(input())
ssum = 0
for a in A:
    if ord(a)-ord('A')<15:
        ssum += (ord(a)-ord('A'))//3 + 3
    else:
        if a in 'PQRS':
            ssum += 8
        elif a in 'TUV':
            ssum += 9
        else:
            ssum += 10
print(ssum)
