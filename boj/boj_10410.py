#eligible한 조건
#1. post-secondary 연구 시작이 2010년 이상
#2. 1991년 이후 태어났을 때
#3. 1, 2 해당없고 40학기 이상 들었을 때는 ineligible
#4. 1,2,3 해당없으면 코치

n = int(input())

for _ in range(n):
    checkEligible = list(map(str, input().split()))

    if int(checkEligible[1][:4]) >= 2010:
        print(checkEligible[0], "eligible", sep=' ')

    elif int(checkEligible[2][:4]) >= 1991:
        print(checkEligible[0], "eligible", sep=' ')

    elif int(checkEligible[3]) >= 41:
        print(checkEligible[0], "ineligible", sep=' ')

    else:
        print(checkEligible[0], "coach petitions", sep=' ')
