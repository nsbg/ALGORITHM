# Bronze 1

import sys

x, y = map(int, sys.stdin.readline().split())

date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayList = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

day = 0

for i in range(x-1):
    day += date[i]

day += y

print(dayList[day % 7])

# < 파이썬 내장 calendar 모듈 사용 방식 >
#
# import calendar
# day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
# a,b=map(int,input().split())
#
# k = calendar.weekday(2007,a,b)
#
# print(day[k])