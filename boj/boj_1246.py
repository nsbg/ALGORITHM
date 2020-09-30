# Silver 5

import sys

'''
n : 경래가 가진 달걀의 수
m : 고객
'''

n, m = map(int, sys.stdin.readline().split())

customer = []

# 변수 두 개만 써도 될 듯?
max, total, cost = 0, 0, 0

for _ in range(m):
    customer.append(int(input()))

sortedCustomer = sorted(customer)

for i in range(m):
    # 남은 사람 수보다 계란이 많을 때
    if m-i < n:
        total = sortedCustomer[i] * (m-i)
    # 사람이 계란보다 많을 때
    else:
        total = sortedCustomer[i] * n

    # 큰 값으로 업데이트
    if max < total:
        cost = sortedCustomer[i]
        max = total

print(cost, max)