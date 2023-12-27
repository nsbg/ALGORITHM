# Silver 5

import sys

person_info = {}

N = int(sys.stdin.readline().strip())

for _ in range(N):
    name, status = sys.stdin.readline().split()

    if status == 'enter':
        person_info[name] = status
    elif status == 'leave':
        person_info.pop(name)
    
print(*sorted(person_info, reverse=True), sep='\n')