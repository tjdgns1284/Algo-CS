from statistics import mean
for i in range(int(input())):
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    average = mean(arr)
    cnt = 0
    for x in arr:
        if x> average:
            cnt +=1
    sol = cnt/n*100
    print('%.3f' % sol + '%')
