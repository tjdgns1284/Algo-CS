import itertools


def solution(numbers):
    answer = []
    cards = list(numbers)
    pers = []
    for i in range(1,len(cards)+1):
        pers += list(map(''.join, itertools.permutations(cards, i)))

    for x in pers:
        if x[0]=='0':
            continue
        x=int(x)
        k = int(x**(1/2))+1
        if x in answer:
            continue
        if x ==1:
            continue
        if x ==2 or x==3:
            answer.append(x)
        else:
            for j in range(2,k):
                if x%j==0:
                    break
            else:
                answer.append(x)

    return len(answer)

numbers ='17'
print(solution(numbers))
