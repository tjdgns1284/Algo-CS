
def solution(board, skill):
    answer = 0
    se=len(board)
    g=len(board[0])
    board= sum(board,[])
    for s in skill:
        fboard=[[s[5] if s[1]<=i<=s[3] and s[2]<=j<=s[4] else 0  for j in range(g)] for i in range(se)]
        fboard=sum(fboard,[])
        if s[0]==1:
            board=[board[i]-fboard[i] for i in range(g*se)]
        else:
            board = [board[i] + fboard[i] for i in range(g * se)]



    print(board)
    for l in board:
        if l>0:
            answer +=1


    return answer

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])
