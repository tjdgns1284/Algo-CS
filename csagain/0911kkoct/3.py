from math import ceil
def solution(fees, records):
    answer = []
    intime={}
    total={}
    for record in records:
        a,b,c= record.split()
        h,m= a.split(':')
        t = int(h)*60+int(m)
        if c =='IN':
            intime[b]=t
        else:
            if b in total:
                total[b] += t - intime[b]
            else:
                total[b] = t - intime[b]
            intime[b] = 23*60+59
    for b,t in intime.items():
        x = 23*60+59 -t
        if b in total:
            total[b] += x
        else:
            total[b] = x
    keys = sorted(total.keys())
    for k in keys:
        a = fees[1]
        if fees[0]<total[k]:
            b = ceil((total[k]-fees[0])/fees[2]) * fees[3]
            a += b
        answer.append(a)



    return answer

a=solution([120, 0, 60, 591],["16:00 0099 IN","16:00 0202 IN","18:00 0099 OUT","18:00 0202 OUT","23:58 0099 IN"])
print(a)