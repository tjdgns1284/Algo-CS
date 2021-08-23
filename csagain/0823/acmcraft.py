

for case in range(int(input())):
    N, K = map(int,input().split())
    B_time= [0] + list(map(int,input().split()))
    act_time = B_time.copy()
    buildingorder=[ list() for _ in range(N+1) ]
    for x in range(K):
        prH,prL = map(int,input().split())
        buildingorder[prH].append(prL)

        if act_time[prL] < act_time[prH] + B_time[prL]:
            
            gap = act_time[prH] + B_time[prL] - act_time[prL]
            act_time[prL] = act_time[prH] + B_time[prL]
            if buildingorder[prL]:
                for i in buildingorder[prL]:
                        act_time[i] += gap
        else:
            continue
        
    W = int(input())
    print(act_time[W])