n = int(input())
i = 1
while True:
    x = 3*i**2 - 3*i + 1
    if n<=x:
        print(i)
        break
    i += 1
    continue