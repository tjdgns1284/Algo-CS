N = 1260

coinlist = [500,100,50,10]
count =  0

for coin in coinlist:
    count += N //coin
    N %=coin

print(count)
