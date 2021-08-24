for i in range(int(input())):
    arr =list(input())
    ssum = 0
    s = 1
    for x in arr:
        if x == 'O':
            ssum += s
            s += 1
        else:
            s =1
    print(ssum)