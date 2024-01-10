# Bronze 2

import sys

N = int(input())

player_list = []
answer = []

for _ in range(N):
    last_name = sys.stdin.readline().strip()
    
    player_list.append(last_name[0])

for player in player_list:
    if player_list.count(player) >= 5:
        answer.append(player)

answer = list(set(answer))
 
if len(answer) > 0:
    print(''.join(sorted(answer)))
else:
    print("PREDAJA")