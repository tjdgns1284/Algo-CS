def dp():
    for i in range(1,n):
        rgb[i][0] += min(rgb[i - 1][1], rgb[i - 1][2])
        rgb[i][1] += min(rgb[i - 1][0], rgb[i - 1][2])
        rgb[i][2] += min(rgb[i - 1][1], rgb[i - 1][0])



n = int(input())
rgb = [[int(x) for x in input().split()] for i in range(n)]
dp()
print(min(rgb[n-1]))