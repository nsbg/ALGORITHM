def solution(phone_book):
    answer = True

    phone_book = sorted(phone_book)
    num = phone_book[0]

    for i in range(1, len(phone_book)):
        if num in phone_book[i][0:len(num)]:
            answer = False
            break

    return answer