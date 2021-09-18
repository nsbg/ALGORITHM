# Silver 5

import sys

N = int(sys.stdin.readline().rstrip())

arr = []

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    arr.append(num)

def mergesort(arr):
    i, j = 0, 0

    result = []

    # 원소의 개수가 하나이면 바로 리턴
    if len(arr) <= 1:
        return arr

    # 분할
    mid = len(arr)//2

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    # 병합
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

sortedNumber = mergesort(arr)

for num in sortedNumber:
    print(num)