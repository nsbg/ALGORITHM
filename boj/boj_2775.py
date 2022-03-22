# Bronze 1

import sys

T = int(input())

for _ in range(T):
    floor = int(input())
    room = int(input())

    person = [i for i in range(1, room+1)]

    for _ in range(floor):
        for idx in range(1, room):
            person[idx] += person[idx-1]   

    print(person[-1])