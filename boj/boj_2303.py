# Silver 5

import sys

from itertools import combinations

N = int(sys.stdin.readline().strip())

player = [0]

for i in range(N):
    number = list(map(int, sys.stdin.readline().split()))
    
    combination_candidate = list(combinations(number, 3))
    
    combination_sum = list(map(int, set(str(sum(t))[-1] for t in combination_candidate)))
    
    player.append(max(combination_sum))

max_indices = [i for i, value in enumerate(player) if value == max(player)]

if len(max_indices) == 1:
    print(max_indices[0])
else:
    print(max_indices[-1])