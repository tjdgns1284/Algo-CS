def solution(record):
    uid = {}
    tmp = []
    answer = []
    for x in record:
        arr = list(x.split())

        if arr[0] == 'Enter':

            uid[arr[1]] = arr[2]
            tmp.append(['e', arr[1]])
        elif arr[0] == 'Leave':

            tmp.append(['l', arr[1]])
        else:
            uid[arr[1]] = arr[2]

    for eluid in tmp:
        x = eluid[1]
        if eluid[0] == 'e':
            come = uid[x]
            answer.append(f'{come}님이 들어왔습니다.')
        else:

            out = uid[x]
            answer.append(f'{out}님이 나갔습니다.')

    return answer

record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))