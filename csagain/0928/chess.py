n,m=map(int,input().split())
board=[list(input()) for _ in range(n)]
line1='WB'*4
line2='BW'*4
line1=list(line1)
line2=list(line2)
b1=[]
b2=[]
for i in range(8):
    if i%2:
        b1.append(line1)
        b2.append(line2)
    else:
        b1.append(line2)
        b2.append(line1)

minc = 1<<32
for x in range(n-7):
    for y in range(m-7):
        cnt1 = 0
        cnt2 = 0
        for i in range(8):
            for j in range(8):
                if board[x+i][y+j] == b1[i][j]:
                    cnt2 += 1
                else:
                    cnt1 += 1

        z = min(cnt1,cnt2)
        if z < minc:
            minc=z
print(minc)