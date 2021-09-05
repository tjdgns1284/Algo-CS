from collections import deque
def solution(priorities, location):

    arr = deque(priorities)
    cnt = 0
    while arr:
        done = 0
        a = arr.popleft()

        for x in arr:
            if x>a:
                arr.append(a)
                break
        else:
            cnt += 1
            done =1
        if location:
            location -=1
        else:
            if done:
                return cnt
            else:
                location = len(arr)-1





