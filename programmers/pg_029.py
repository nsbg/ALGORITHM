def solution(s):
    answer = True

    p = 0
    y = 0

    makeLower = s.lower()

    for ml in makeLower:
        if ml == 'p':
            p += 1
        elif ml == 'y':
            y += 1

    if p == y or (p == 0 and y == 0):
        return True
    else:
        return False