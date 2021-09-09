def solution(lines):
    log=[]
    answer = 0
    for line in lines:
        date,s,t=line.split()
        s = s.split(':')
        t= t.replace('s','')
        end = (int(s[0])*3600+int(s[1])*60+float(s[2]))*1000
        start = end - float(t)*1000 +1
        log.append([start,end])

    for x in log:
        answer = max(answer, throughput(log,x[0],x[0]+1000), throughput(log,x[1],x[1]+1000))

    return answer
def throughput(log,start,end):
    cnt= 0
    for x in log:
        if x[0]<end and x[1]>=start:
            cnt +=1
    return cnt
a =solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
])
print(a)