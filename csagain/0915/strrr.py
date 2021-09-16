def apppendstar(n):
    if n==1:
        return ['*']
    stars = apppendstar(n//3)
    res = []

    for s in stars:
        res.append(s*3)
    for s in stars:
        res.append(s+' '*(n//3)+s)
    for s in stars:
        res.append(s*3)
    return res

n = int(input())
print('\n'.join(apppendstar(n)))