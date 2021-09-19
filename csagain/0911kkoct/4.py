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
            k = o
        else:
            x = o
            v = 1
            xv = o
            k = 0
        values.append([xv, o, v])
        freroll.append([o, k, v])

    values.sort(key=lambda x: (-x[0], -x[1]))

    for value in values:
        if value[1] == 0:
            answer[10] = n

            break
        if n >= value[2]:
            answer[10 - value[1]] = value[2]
            n -= value[2]
        if n == 0:
            break

    appeach = 0
    ryan = 0
    for i in range(11):
        if info[i] == 0 and answer[i] == 0:
            continue
        if info[i] >= answer[i]:
            appeach += 10 - i
        else:
            ryan += 10 - i
    sol = ryan - appeach
    if sol <= 0:
        return [-1]

    for i in range(10):

        n = n_c - answer[10]
        new_answer = [0 for _ in range(11)]
        new_answer[10] = answer[10]
        new_answer[9-i] = freroll[9-i][2]
        n -= new_answer[9-i]


        for value in values:
            if value[1] <= i:
                continue
            if value[1] == 0:
                break
            if n >= value[2]:
                new_answer[10 - value[1]] = value[2]
                n -= value[2]
            if n == 0:
                break
        appeach = 0
        ryan = 0
        for i in range(11):
            if info[i] == 0 and new_answer[i] == 0:
                continue
            if info[i] >= new_answer[i]:
                appeach += 10 - i
            else:
                ryan += 10 - i
        new_sol = ryan - appeach
        if sol <= new_sol:
            change = 0
            for i in range(11):
                if answer[10 - i] == new_answer[10 - i]:
                    continue
                elif answer[10 - i] > new_answer[10 - i]:
                    break
                else:
                    change = 1
                    break
            if change:
                answer = new_answer
                sol = new_sol

    return answer