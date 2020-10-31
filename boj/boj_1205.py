# Silver 4

import sys

# p : 랭킹 리스트에 올라갈 수 있는 점수 개수
n, newScore, p = map(int, sys.stdin.readline().split())

rank = list(map(int, sys.stdin.readline().split()))

rank.append(newScore)

rank = sorted(rank, reverse=True)

# 새 점수가 랭킹 리스트 벗어나거나 랭킹 리스트가 꽉 찼는데 마지막 점수랑 같을 때
if rank.index(newScore) > p or (n == p and rank[-1] == newScore):
    print("-1")
# 등수를 매길 수 있을 때
else:
    print(rank.index(newScore)+1)