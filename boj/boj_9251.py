# Gold 5

# 메모리 초과
# from itertools import combinations

# S = input()
# T = input()

# min_length = min(len(S), len(T))

# s_combination, t_combination = [], []

# for i in range(1, min_length+1):
#     s_combination.extend(list(combinations(S, i)))
#     t_combination.extend(list(combinations(T, i)))

# s_combination = set([''.join(item) for item in s_combination])
# t_combination = set([''.join(item) for item in t_combination])

# intersection = sorted(list(set(s_combination & t_combination)), key=len)

# if len(intersection) == 0:
#     print(0)
# else:
#     print(len(intersection[-1]))

A = input()
B = input()

dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(A)][len(B)])