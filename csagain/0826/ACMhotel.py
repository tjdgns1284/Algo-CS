for T in range(int(input())):
    h,w,n = map(int,input().split())
    k = n//h
    if n%h ==0:
        k -= 1
    a = n - k*h
    k+=1
    if k >=10:
        print(f'{a}{k}')
    else:
        print(f'{a}0{k}')
