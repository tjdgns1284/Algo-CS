arr= [1 for _ in range(10001)]
for x in range(1,10001):
    new_x = x + x//1000 + (x%1000)//100 + (x%100)//10 +x%10
    if new_x>10000:
        continue
    else:
        arr[new_x] = 0
for i in range(1,len(arr)):

    if arr[i]:
        print(i)
