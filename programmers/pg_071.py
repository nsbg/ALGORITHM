# Level 1

def solution(s):
    answer = []
    
    idx = {}
    
    for i in range(0, len(s)):
        if s[i] not in idx:
            answer.append(-1)
        else:
            answer.append(i-idx[s[i]])
        
        idx[s[i]] = i # 인덱스 갱신
        
    return answer