import sys

# type : list
user = input().split()

candidates = []

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    userList = sys.stdin.readline().split()

    if userList[1] == user[1]:
        if int(userList[2]) <= int(user[2]):
            candidates.append(userList[0])

    if user[1] == "FM" or user[1] == "MF":
        if int(userList[2]) <= int(user[2]):
            candidates.append(userList[0])

candidates.sort()

if len(candidates) > 0:
    print(*candidates, sep="\n")
else:
    print("No one yet")
