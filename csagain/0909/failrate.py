def solution(N, stages):
    answer = []
    x = [[i] for i in range(1,N+1)]
    fails = [0 for _ in range(N+1)]
    for stage in stages:
        if stage<=N:
            fails[stage]+=1
    fails.pop(0)
    m = len(stages)
    for i in range(len(fails)):
        if m==0:
            x[i].append(0)
            continue
        x[i].append(fails[i]/m)
        m -=fails[i]
    x.sort(key= lambda x: (-x[1],x[0]))
    for k in x:
        answer.append(k[0])
    return answer