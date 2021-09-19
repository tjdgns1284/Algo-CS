def solution(info, edges):
    answer = 0
    par = [0 for _ in range(len(info))]
    son = [[] for _ in range(len(info))]
    for edge in edges:
        son[edge[0]].append(edge[1])
        par[edge[1]] = edge[0]
    for i in range(len(info)):
        if son[i]:
            continue
        else:
            if info[i]:
                info[i]= 2


    return answer