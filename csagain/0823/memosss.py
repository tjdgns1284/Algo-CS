a, b = map(int, input().split())
print(a/b)


n = int(input())
for i in range(1,10):
    print(f'{n} * {i} = {n*i}')


test = int(input())
if test>=90:
    print('A')
elif test>=80:
    print('B')
elif test>=70:
    print('C')
elif test>=60:
    print('D')
else:
    print('F')