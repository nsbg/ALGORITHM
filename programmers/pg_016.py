# Level 1

def solution(a, b):
    endOfMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]

    # 1월부터 (a-1)월까지 총 날짜 수 계산
    cnt = 0

    for i in range(0, a - 1):
        cnt += endOfMonth[i]

    return day[(cnt + b) % 7]