a,b = input().split()
A = list(a)
A[0],A[2] = A[2], A[0]
B = list(b)
B[0],B[2] = B[2], B[0]
for i in range(2):
    if int(A[i]) > int(B[i]):
        print(''.join(A))
        break
    elif int(A[i]) == int(B[i]):
        continue
    else:
        print(''.join(B))
        break
