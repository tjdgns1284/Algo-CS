n = int(input())
scores = list(map(int,input().split()))
M = max(scores)
ssum = 0
for score in scores:
    new_score = score/M*100
    ssum += new_score
print(ssum/n)