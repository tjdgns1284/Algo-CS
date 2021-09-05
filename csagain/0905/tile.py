def solution(brown, yellow):
    k = brown //2
    answer = []
    for i in range(3,k+1):
        for j in range(3,i+1):
            if 2*(i+j)-4>brown:
                break
            elif brown ==2*(i+j)-4:
                if (i-2)*(j-2)==yellow:
                    answer=[i,j]
                    break
                else:
                    continue
            else:
                continue
        if answer:
            break

    return answer

print(solution(10,2))