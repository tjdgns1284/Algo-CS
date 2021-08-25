croat = 'cdlnsz'
croatss = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
skip = 0
ssum = 0
for i in range(len(word)):
    if skip:
        skip -= 1
        continue
    if word[i] in croat:
        if i < len(word) - 2:
            a = word[i] + word[i+1]
            b = word[i] + word[i+1] + word[i+2]
        elif i == len(word)-2:
            a = word[i] + word[i+1]
            b = 'nope'
        else:
            ssum += 1
            continue
        if a in croatss:
            ssum += 1
            skip = 1
            continue
        if b in croatss:
            ssum += 1
            skip =2
            continue
        ssum += 1
        skip = 0

    else:
        ssum +=1
        skip =0
        continue
print(ssum)
