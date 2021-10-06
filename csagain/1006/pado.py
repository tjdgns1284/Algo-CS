mem = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for T in range(int(input())):
    n= int(input())
    while n>len(mem):
        mem.append(mem[-1] + mem[-5])

    print(mem[n-1])