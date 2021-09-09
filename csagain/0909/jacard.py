def solution(str1, str2):
    answer = 0
    l1 = []
    l2 = []
    for i in range(len(str1) - 1):
        if 65 <= ord(str1[i]) <= 90:
            a = chr(ord(str1[i]))
        elif 97 <= ord(str1[i]) <= 122:
            a = chr(ord(str1[i]) - 32)
        else:
            continue
        if 65 <= ord(str1[i + 1]) <= 90:
            b = chr(ord(str1[i + 1]))
        elif 97 <= ord(str1[i + 1]) <= 122:
            b = chr(ord(str1[i + 1]) - 32)
        else:
            continue
        x = a + b
        l1.append(x)
    for i in range(len(str2) - 1):
        if 65 <= ord(str2[i]) <= 90:
            a = chr(ord(str2[i]))
        elif 97 <= ord(str2[i]) <= 122:
            a = chr(ord(str2[i]) - 32)
        else:
            continue
        if 65 <= ord(str2[i + 1]) <= 90:
            b = chr(ord(str2[i + 1]))
        elif 97 <= ord(str2[i + 1]) <= 122:
            b = chr(ord(str2[i + 1]) - 32)
        else:
            continue
        x = a + b
        l2.append(x)
    l1.sort()
    l2.sort()
    i, j = 0, 0
    cnt = 0
    m = len(l1)
    n = len(l2)
    while True:
        if i == m:
            break
        if j == n:
            break
        if l1[i] == l2[j]:
            i += 1
            j += 1
            cnt += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            i += 1

    if m + n - cnt == 0:
        answer = 65536
    else:
        answer = int(cnt / (m + n - cnt) * 65536)
    return answer