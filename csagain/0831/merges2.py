import sys

input = sys.stdin.readlines
print = sys.stdout.write
from collections import deque


def mergesort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)


def merge(left, right):
    result = deque()
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(right[0])
                right.popleft()
            else:
                result.append(left[0])
                left.popleft()
        elif len(left) > 0:
            result.append(left[0])
            left.popleft()
        elif len(right) > 0:
            result.append(right[0])
            right.popleft()
    return result


n = int(input())
arr = deque(map(int, input().split()))
arr = mergesort(arr)

