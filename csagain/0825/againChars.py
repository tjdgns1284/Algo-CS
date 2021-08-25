for T in range(int(input())):
    a,B = input().split()
    a = int(a)
    sol = ''
    for c in B:
        sol += c*a
    print(sol)