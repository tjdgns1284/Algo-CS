for T in range(int(input())):
    k = int(input())
    n = int(input())
    i = 0
    arr = [i for i in range(1,n+1)]
    for _ in range(k):
        new_arr = [1] +[0 for _ in range(n-1)]
        for x in range(1,n):
            new_arr[x] = new_arr[x-1] +arr[x]
        arr = new_arr.copy()
    print(arr[n-1])

