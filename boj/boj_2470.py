# Gold 5

n = int(input())

# [-99, -2, -1, 4, 98]
potion = sorted(list(map(int, input().split())))

start, end = 0, n-1

result = [0, 0]

# 초기값은 -1
compare = potion[start]+potion[end]

while start < end:
    tmp = potion[start] + potion[end]

    if abs(tmp) <= abs(compare):
        compare = tmp

        result[0] = potion[start]
        result[1] = potion[end]

        if abs(tmp) == 0:
            break
    
    if tmp > 0:
        end -= 1
    else:
        # 첫번째 tmp = -1
        # 두번째 tmp = 96
        start += 1
    
print(result[0], result[1])