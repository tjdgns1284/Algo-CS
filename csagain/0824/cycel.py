n = int(input())
new_n = n
cycle = 0
while True:
    cycle += 1
    a = new_n//10
    b = new_n%10
    c = a+b
    new_n = b*10 + c%10
    if new_n == n:
        break
print(cycle)