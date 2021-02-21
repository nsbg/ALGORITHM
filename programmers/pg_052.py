def solution(board, moves):
    basket = []
    moves = [i - 1 for i in moves]
    answer = 0

    for m in moves:
        for i in range(len(board)):
            if board[i][m] != 0:
                basket.append(board[i][m])
                board[i][m] = 0

                if len(basket) > 1:
                    # 인덱스 뒤부터 접근하는 방식 기억하기
                    if basket[-2] == basket[-1]:
                        basket.pop(-2)
                        basket.pop(-1)

                        answer += 2
                break
            else:
                pass

    return answer