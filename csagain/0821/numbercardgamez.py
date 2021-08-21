n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
ans = 0

for line in board:
    smallest = 1 << 32
    for num in line:
        if num < smallest:
            smallest = num
    if smallest > ans:
        ans = smallest
print(ans)
