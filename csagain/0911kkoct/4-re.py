def solution(n, info):
    answer = [0 for _ in range(11)]
    values = []
    n_c = n
    freroll = []
    for i in range(11):
        o = 10 - i
        if info[i]:
            x = 2 * o
            if o:
                v = info[i] + 1
            else:
                v = 1
            xv = x / v
            k=o
        else:
            x = o
            v = 1
            xv = o
            k=0
        values.append([xv, o, v])
        freroll.append([o,k,v])