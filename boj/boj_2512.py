# Silver 3

# < 문제 풀이 흐름 >
# 1. low=0, high=입력 받은 금액 중 가장 큰 금액
# 2. mid=(low+high)/2
# 3. 예산 총액이 정해진 예산을 넘으면 high=mid-1
# 4. 예산 총액이 정해진 예산보다 적으면 low=mid+1
# 5. low < high인 동안 while문 돌리기

import sys

n = int(input())

budget = list(map(int, sys.stdin.readline().split()))

low = 0
high = max(budget)

budgetSum = int(input())

while low <= high:
    total = 0
    mid = (low + high) // 2

    for i in budget:
        total += min(mid, i)

    if total > budgetSum:
        high = mid-1
    else:
        low = mid+1

print(high)