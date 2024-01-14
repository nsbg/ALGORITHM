# Gold 5

import sys

from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

city = [list(sys.stdin.readline().split()) for _ in range(N)]

home = []
chicken_distance = []

city_chicken_distance = 1000000

for row in range(len(city)):
    for col in range(len(city)):
        if city[row][col] == '1':
            home.append([row, col])
        elif city[row][col] == '2':
            chicken_distance.append([row, col])

for chicken_idx in list(combinations(chicken_distance, M)):
    temp = 0
    
    for home_idx in home:
        distance = 1000000
        
        for i in range(M):
            distance = min(abs(home_idx[0]-chicken_idx[i][0])+abs(home_idx[1]-chicken_idx[i][1]), distance)

        temp += distance
        
    city_chicken_distance = min(temp, city_chicken_distance)

print(city_chicken_distance)