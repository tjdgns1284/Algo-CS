for case in range(int(input())):
    a,b= map(int,input().split())
    gap =b-a
    cnt = 0
    max_d =0
    now_k=0
    while True:
        cnt += 1
        if cnt%2:
            now_k+=1
        max_d += now_k
        if gap<=max_d:
            print(cnt)
            break