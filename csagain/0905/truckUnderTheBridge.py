from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    tmp = deque(truck_weights.copy())
    arr = list(0 for _ in range(bridge_length))
    queue= deque(arr)
    otb = 0
    while queue:
        answer += 1
        a = queue.popleft()
        if a:
            otb -= a
        if tmp:
            if otb + tmp[0]<=weight:
                x = tmp.popleft()
                queue.append(x)
                otb += x
            else:
                queue.append(0)
        else:
            answer += len(queue)
            break


    return answer