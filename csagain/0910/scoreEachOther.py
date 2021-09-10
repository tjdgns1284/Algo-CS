def validationcheck(n,arr):
    k = arr[n]
    is_max = 0
    is_min = 101

    for i in range(len(arr)):
        if i==n:
            continue
        if arr[i]>=is_max:
            is_max = arr[i]
        if arr[i]<=is_min:
            is_min = arr[i]
    if is_max<k:
        arr.pop(n)
    elif is_min>k:
        arr.pop(n)
    return arr
def solution(scores):
    answer = ''
    get_scores = [[0 for __ in range(len(scores)) ] for _ in range(len(scores))]
    for i in range(len(scores)):
        for j in range(len(scores)):
            get_scores[i][j] = scores[j][i]
    for idx,score in enumerate(get_scores):
        new_arr = validationcheck(idx,score)
        avg= sum(new_arr)/len(new_arr)
        if avg>=90:
            answer += 'A'
        elif avg>=80:
            answer += 'B'
        elif avg>=70:
            answer += 'C'
        elif avg>=50:
            answer += 'D'
        else:
            answer += 'F'
    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
