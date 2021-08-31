n=int(input())
ages=[0 for _ in range(201)]
names = [ [] for _ in range(201)]
for _ in range(n):
    age, name = map(str,input().split())
    age=int(age)
    ages[age]+=1
    names[age].append(name)
for i in range(201):
    if ages[i]:
        for j in names[i]:
            print(f'{i} {j}')
