# Silver 5

import sys

N = int(sys.stdin.readline().strip())

name = []

for _ in range(N):
    name.append(sys.stdin.readline().strip())

decreasing_name = sorted(name, reverse=True) # 내림차순
increasing_name = sorted(name)               # 오름차순

if name == decreasing_name:
    print("DECREASING")
elif name == increasing_name:
    print("INCREASING")
else:
    print("NEITHER")