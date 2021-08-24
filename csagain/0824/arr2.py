idx = 0
max = 0
for i in range(9):
    x = int(input())
    if x > max:
        max = x
        idx = i+1
print(max)
print(idx)