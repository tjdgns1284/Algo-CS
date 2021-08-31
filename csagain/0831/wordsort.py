n=int(input())
arr= [[] for _ in range(51)]
for _ in range(n):
    word = input()
    if word not in arr[len(word)]:
        arr[len(word)].append(word)

for i in range(51):
    if arr[i]:
        arr[i].sort()
        for word in arr[i]:
            print(word)
