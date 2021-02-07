def solution(people, limit):
    answer = 0
    people.sort()

    front = 0
    back = len(people) - 1

    while front <= back:
        if people[front] + people[back] > limit:
            answer += 1
            back -= 1
        else:
            answer += 1
            front += 1
            back -= 1

    return answer