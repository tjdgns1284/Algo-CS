n = int(input())
arr = list(map(int,input().split()))
largest = -1<<32
smallest = 1<<32
for x in arr:
    if x > largest:
        largest = x
    if x < smallest:
        smallest =x
print(f'{smallest} {largest}')
