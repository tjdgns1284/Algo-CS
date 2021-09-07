from itertools import combinations
def solution(orders, course):
    answer = []
    real_orders=[]
    for order in orders:
        x = list(order)
        x.sort()
        real_orders.append(x)
    for n in course:
        di= {}
        for x in real_orders:
            k= len(x)

            if n>k:
                continue
            for y in list(combinations(x,n)):
                tmp= ''.join(y)
                if di.get(tmp):
                    di[tmp]+=1
                else:
                    di[tmp]=1
        possible=[]
        maxn=2

        for key,val in di.items():
            if val>maxn:
                maxn=val
                possible=[key]
            elif val==maxn:
                possible.append(key)

        answer.extend(possible)
        answer.sort()
    return answer

# a=solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])
b=solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
# print(a)
print(b)