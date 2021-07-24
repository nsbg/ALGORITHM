# Silver 4
# 시간이 2.7초 정도 걸려서 효율이 좋은 코드는 아님

n = int(input())

extension = dict()

for _ in range(n):
    filename = input().split('.')

    if filename[1] not in extension.keys():
        extension[filename[1]] = 1
    else:
        extension[filename[1]] += 1
    
sortedDict = sorted(extension.items())

for s in sortedDict:
    print(s[0], s[1])