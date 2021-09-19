def solution(id_list, report, k):
    answer = []
    id_report= {}
    id_count ={}
    for id in id_list:
        id_report[id]=[]
        id_count[id]=0
    report = list(set(report))
    for rep in report:


        a,b= rep.split()
        id_report[a].append(b)
        id_count[b] += 1

    for id in id_report.values():
        cnt = 0
        for x in id:
            if id_count[x]>=k:
                cnt += 1
        answer.append(cnt)


    return answer