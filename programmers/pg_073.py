# Level 2

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
        
    return a
            
def solution(arr):
    answer = arr[0]
    
    for i in range(1, len(arr)):
        answer *= arr[i]//gcd(answer, arr[i])
            
    return answer