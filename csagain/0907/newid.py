def solution(new_id):
    queue=[]
    last =1
    for x in new_id:
        n= ord(x)
        if 97<=n<=122 or n in [45,95]:
            queue.append(x)
        elif n in [48,49,50,51,52,53,54,55,56,57]:
            queue.append(x)
        elif 65<=n<=90:
            x= chr(n+32)
            queue.append(x)
        elif n==46 and last:
            queue.append(x)
            last = 0
            continue
        else:
            continue
        last =1
    if queue:
        if last==0:
            queue.pop()
    if queue:
        if queue[0]=='.':
            queue.pop(0)
    if queue==[]:
        queue.append('a')

    if len(queue)>=16:
        queue= queue[:15]
        if queue[14]=='.':
            queue.pop()
    while len(queue)<3:
        queue.append(queue[-1])



    answer=''.join(queue)
    return answer

# print(solution('.aaBNA.....q45//*!.'))
# print(solution('..'))
# print(solution('abcdefghijklmnopqrstuvwxyz'))
print(solution('z-+.^.'))