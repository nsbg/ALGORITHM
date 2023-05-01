# Level 2

def solution(n):
    answer = 0
    
    n_sum = [i for i in range(0, n+2)]
    
    for i in range(1, n):
        n_sum[i] += n_sum[i-1]
    
    start, end = 0, 0

    while start <= end:
        if end > n-1:
            break
        
        check = n_sum[end]-n_sum[start]

        if check < n:
            end += 1
        elif check > n:
            start += 1
        else:
            answer += 1
            start += 1
        
    return answer+1